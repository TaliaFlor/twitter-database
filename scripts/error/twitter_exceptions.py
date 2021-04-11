class TwitterException(Exception):

    def __init__(self, message):
        super(TwitterException, self).__init__(message)
        self.message = message

    def get_message(self):
        return self.message


class TwitterExceptionCollection(Exception):
    """A collection of TwitterExceptions"""

    def __init__(self):
        """Initializes the collection"""
        super(TwitterExceptionCollection, self).__init__()
        self.exceptions = []

    def add(self, twitter_exception):
        """Adds an exception to the collection"""
        self.exceptions.append(twitter_exception)

    def validate(self):
        """If at least one exception exists, it is not valid"""
        if self.is_exceptions_exist():
            raise self

    def is_exceptions_exist(self):
        """Returns true if at least one exception exists"""
        return len(self.exceptions) > 0
