from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Tweet:
    """Represents a tweet post. Can be an original post, a reply or a quote"""
    tweet_id: int
    user_id: int
    content: str
    reply_id: int = None
    quote_id: int = None
    posted_on: datetime = None
