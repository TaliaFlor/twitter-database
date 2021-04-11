from dataclasses import dataclass


@dataclass(frozen=True)
class Like:
    """Represents a like given to a tweet"""
    tweet_id: int
    user_id: int
