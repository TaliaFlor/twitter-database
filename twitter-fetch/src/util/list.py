from src.models.tweet import Tweet
from src.models.user import User


def exists(_list: list, id: int) -> bool:
    return find_by_id(_list, id) is not None


def find_by_id(_list: list, id: int) -> object:
    for item in _list:
        if isinstance(item, User) and item.user_id == id:
            return item
        elif isinstance(item, Tweet) and item.tweet_id == id:
            return item
        else:
            return None
