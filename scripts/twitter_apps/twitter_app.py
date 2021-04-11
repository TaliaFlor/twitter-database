from twitter import *

from scripts.basic.basic_app import BasicApp


class TwitterApp(BasicApp):
    """Connects with Twitter"""

    def __init__(self, configuration_filename):
        super(TwitterApp, self).__init__(configuration_filename)

    def get_oauth(self):
        """
        Reads the Twitter credentials from the configuration file
        and authenticates them.
        """
        self.logger.debug('Getting oauth information...')
        main_configuration = self.main_configuration
        twitter_configuration = main_configuration["twitter_configuration"][0]
        access_token = twitter_configuration["access_token"]
        access_token_secret = twitter_configuration["access_token_secret"]
        api_key = twitter_configuration["api_key"]
        api_secret = twitter_configuration["api_secret"]
        oauth = OAuth(access_token, access_token_secret, api_key, api_secret)
        return oauth
