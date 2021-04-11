import sys

from scripts.error.twitter_exceptions import *


class ErrorManager:
    """Manages the application errors"""

    def __init__(self):
        """Initializes the errors collection"""
        self.errors = TwitterExceptionCollection()

    def add(self, message=None):
        """Adds the current error to the collection"""
        if message is None:
            message = sys.exc_info()[0]
        twitter_exception = TwitterException(message)
        self.errors.add(twitter_exception)

    def validate(self):
        """Validates if no error ocurred. If it did, raises an exception."""
        self.errors.validate()

    def is_errors_exist(self):
        """Returns true if at least one error exists."""
        return self.errors.is_exceptions_exist()
