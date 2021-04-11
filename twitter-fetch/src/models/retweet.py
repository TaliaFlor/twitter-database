from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Retweet:
    """Represents a retweet of a tweet"""
    tweet_id: int
    user_id: int
    retweeted_on: datetime
