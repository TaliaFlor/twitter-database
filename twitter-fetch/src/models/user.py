from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    """Represents a Twitter user"""
    user_id: int
    email: str
    password: str
    username: str
    display_name: str
    location: str = None
    description: str = None
    verified: bool = False
    joined_on: datetime = None
