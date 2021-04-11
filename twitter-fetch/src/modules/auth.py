from twitter import OAuth

from src.util import read_file


def get_oauth(filename):
    credentials = read_file(filename)
    oauth = OAuth(
        token=credentials["token"],
        token_secret=credentials["token_secret"],
        consumer_key=credentials["consumer_key"],
        consumer_secret=credentials["consumer_secret"]
    )
    return oauth
