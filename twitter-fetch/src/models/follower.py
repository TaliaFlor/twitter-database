from dataclasses import dataclass


@dataclass(frozen=True)
class Follower:
    """Represents a follower of a user"""
    user_id: int
    follower_id: int
