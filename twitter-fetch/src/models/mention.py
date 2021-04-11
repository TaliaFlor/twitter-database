from dataclasses import dataclass


@dataclass(frozen=True)
class Mention:
    """Represents a mention of a user in a tweet"""
    tweet_id: int
    user_id: int
