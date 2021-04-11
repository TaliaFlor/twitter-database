from src.api.parser import Parser


class Collection:
    """Contains colletions with all the data parsed"""

    def __init__(self, parser: Parser):
        self.users = []
        self.retweets = []
        self.tweets = []
        self.hashtags = []
        self.mentions = []
        self.followers = []
        self.likes = []

        self.parser = parser

    # ------- PUBLIC METHODS  -------

    def collect(self):
        self.users, \
        self.retweets, \
        self.tweets, \
        self.hashtags, \
        self.mentions, \
        self.followers, \
        self.likes = self.parser.parse()

    # ------- PRIVATE METHODS  -------
