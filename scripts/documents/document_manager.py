from ast import parse

from bson.int64 import long
from pymongo import MongoClient


class DocumentManager:
    """Manages the dabatase manipulation"""

    def __init__(self, database_configuration):
        """Setups the collections"""
        self.database_configuration = database_configuration
        self.database = self.__get_database()
        self.tweets_collection = self.__get_tweets_collection()
        self.users_collection = self.__get_users_collection()

    # ===== PRIVATE METHODS =====

    def __get_database(self):
        """Connects to the database"""
        database_configuration = self.database_configuration
        username = database_configuration["username"]
        password = database_configuration["password"]
        host = database_configuration["host"]
        port = database_configuration["port"]
        database = database_configuration["database"]
        uri = f'mongodb://{username}:{password}@{host}:{port}/{database}'  # TODO change to mySQL
        mongodb_client = MongoClient(uri)
        db = mongodb_client[database]
        return db

    def __get_tweets_collection(self):
        """Gets the collection in which the tweets are guarded"""
        return self.__get_collection("tweets_collection")

    def __get_users_collection(self):
        """Gets the collection in which the users are guarded"""
        return self.__get_collection("users_collection")

    def __get_collection(self, collection_type):
        """Returns a specific collection"""
        database_configuration = self.database_configuration
        collection_configuration = database_configuration["collection_configuration"]
        collection_name = collection_configuration[collection_type]
        db = self.database
        collection = db[collection_name]
        return collection

    # ===== PUBLIC METHODS =====

    def insert_tweet(self, tweet):
        self.tweets_collection.insert_one(tweet)

    def insert_user(self, user):
        self.users_collection.insert_one(user)

    def get_tweets(self, skip=None, limit=None):
        tweets = self.__get_tweets_collection().find(timeout=False)
        tweets = self.get_limited_skipped(tweets, skip=skip, limit=limit)
        return tweets

    def get_retweets_collection(self):
        return self.__get_collection("retweets_collection")

    def get_next_unvisited_tweet(self):
        tweets_collection = self.tweets_collection
        next_tweet = tweets_collection.find_one({"timestamp_ms": "0"})
        return next_tweet

    def is_user_friends_exists(self, user_id):
        pass

    def is_user_exists(self, user_id):
        users_found = self.get_users(user_id)
        return users_found.count() > 0

    def create_user(self, user):
        self.__get_users_collection().insert({
            "id": user["id"],
            "screen_name": user["screen_name"].encode('utf-8'),
            "followers_count": user["followers_count"],
            "friends_count": user["friends_count"]})

    def is_retweet_exists(self, tweet):
        return self.get_retweets(tweet).count() > 0

    def create_retweet(self, retweet):
        tweet = retweet["retweeted_status"]
        retweet_created_at = parse(retweet["created_at"])
        tweet_created_at = parse(tweet["created_at"])
        retweet_tweet_diff_time = retweet_created_at - tweet_created_at
        self.get_retweets_collection().insert({
            "id": retweet["_id"],
            "retweet_id": retweet["id"],
            "retweet_user_id": retweet["user"]["id"],
            "retweet_user_name": retweet["user"]["name"],
            "retweet_coordinates": retweet["coordinates"],
            "retweet_created_at": retweet_created_at,
            "tweet_id": tweet["id"],
            "tweet_user_id": tweet["user"]["id"],
            "tweet_user_name": tweet["user"]["name"],
            "tweet_coordinates": tweet["coordinates"],
            "tweet_created_at": tweet_created_at,
            "tweet_retweet_count": tweet["retweet_count"],
            "retweet_tweet_diff_time": float(retweet_tweet_diff_time.total_seconds())
        })

    def get_users(self, user_id):
        return self.__get_users_collection().find({"id": long(user_id)}, timeout=False)

    def get_user(self, user_id):
        return self.__get_users_collection().find({"id": long(user_id)}, timeout=False).limit(1)

    def get_retweets(self, retweet=None, skip=None, limit=None):
        criteria = {}
        if retweet is not None:
            criteria = {
                "$or": [
                    {"id": retweet["_id"]},
                    {"$and": [
                        {"retweet_id": retweet["id"]},
                        {"tweet_id": retweet["retweeted_status"]["id"]}
                    ]}
                ]
            }
        retweets_cursor = self.get_retweets_collection().find(criteria, timeout=False)
        retweets_cursor = self.get_limited_skipped(retweets_cursor, skip, limit)
        return retweets_cursor

    def get_retweeted_tweets(self, skip=None, limit=None):
        retweets_cursor = self.__get_tweets_collection().find({"retweeted_status": {"$ne": None}}, timeout=False)
        retweets_cursor = self.get_limited_skipped(retweets_cursor, skip, limit)
        return retweets_cursor

    def get_limited_skipped(self, collection, skip=None, limit=None):
        limited_skipped_collection = collection
        if skip is not None:
            limited_skipped_collection = limited_skipped_collection.skip(skip)
        if limit is not None:
            limited_skipped_collection = limited_skipped_collection.limit(limit)
        return limited_skipped_collection
