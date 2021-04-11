from dataclasses import dataclass


@dataclass(frozen=True)
class Hashtag:
    """Represents a hashtag used in a tweet"""
    tweet_id: int
    hashtag: str
