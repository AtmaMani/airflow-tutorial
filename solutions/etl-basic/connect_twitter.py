# Import libraries needed
from configparser import ConfigParser
from pathlib import Path

import tweepy

# Path to the config file with the keys make sure not to commit this file
CONFIG_FILE = Path.cwd() / "config.cfg"

config = ConfigParser()
config.read(CONFIG_FILE)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    config.get("twitter", "consumer_key"), config.get("twitter", "consumer_secret")
)
auth.set_access_token(
    config.get("twitter", "access_token"), config.get("twitter", "access_token_secret")
)

# Create Twitter API object
twitter = tweepy.API(auth)

# let's collect some of the tweets in your public timeline
public_tweets = twitter.home_timeline()

for tweet in public_tweets:
    print()
    print(tweet.text)
