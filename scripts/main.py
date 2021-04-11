from twitter_apps.twitter_track_app import TwitterTrackApp

configuration_filename = "configuration_files/config.json"

try:
    twitter_tracker = TwitterTrackApp(configuration_filename)
    twitter_tracker.start()
except Exception as exp:
    print(exp)
