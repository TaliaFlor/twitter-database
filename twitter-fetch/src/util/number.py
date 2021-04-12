import random
from datetime import datetime


# ======== DATE =======

def fmt_date(_date: str):
    """Normalizes a date to a format the database recognizes"""
    return __get_datetime_obj(_date).strftime('%Y-%m-%d')


def fmt_datetime(_datetime: str):
    """Normalizes a date to a format the database recognizes"""
    return __get_datetime_obj(_datetime).strftime('%Y-%m-%d %H:%M:%S')


def __get_datetime_obj(str_date: str):
    return datetime.strptime(str_date, '%a %b %d %H:%M:%S %z %Y')


# ======== RANDOM =======

def randmedium(_list: list):
    """Returns a random number between 25-75% of the size of a given list"""
    return random.randint(one_quarter(_list), three_quarters(_list))


def one_quarter(_list: list) -> int:
    """Retorna quantos itens equivalem a 25% de uma lista"""
    half = len(_list) / 2
    return round(half / 2)


def three_quarters(_list: list) -> int:
    """Retorna quantos itens equivalem a 75% de uma lista"""
    half = len(_list) / 2
    one_quarter = half / 2
    return round(half + one_quarter)
