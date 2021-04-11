import time

from twitter import *

from scripts.twitter_apps.twitter_app import TwitterApp


class TwitterTrackApp(TwitterApp):
    """Consumes from twitter"""

    def __init__(self, configuration_filename):
        super(TwitterTrackApp, self).__init__(configuration_filename)
        self.twitter_stream = self.__get_twitter_stream()
        self.track_words = self.__get_track_words()

    # ===== PRIVATE METHODS =====

    def __get_twitter_stream(self):
        """Initializes the Twitter stream"""
        self.logger.debug('Getting twitter stream...')
        oauth = self.get_oauth()
        twitter_stream = TwitterStream(auth=oauth)
        return twitter_stream

    def __get_track_words(self):
        """Gets the keywords to be tracked from the configuration file"""
        main_configuration = self.main_configuration
        application_configuration = main_configuration["application_configuration"]
        track_words = application_configuration["track_words"]
        return track_words

    # ===== PUBLIC METHODS =====

    def start(self):
        """Starts tracking the tweets"""
        twitter_stream = self.twitter_stream
        document_manager = self.document_manager
        track_words = self.track_words
        self.logger.debug('Listener running...')
        while True:
            try:
                stream = twitter_stream.statuses.filter(track=track_words)
                for tweet in stream:
                    document_manager.insert_tweet(tweet)
                break
            except Exception as e:
                self.logger.critical(e)
                time.sleep(60)
        self.logger.info('Program finished')
