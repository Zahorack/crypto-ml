from abc import ABC
from typing import Iterator, Optional
from dataclasses import dataclass
import tweepy

from crypto_ml.api import ApiHandler
from crypto_ml.api import ApiSample
from crypto_ml import config


@dataclass
class TwitterSample:
    text: str
    user_name: str
    user_statuses_count: str
    user_followers_count: str
    user_location: str
    user_verified: str
    favorite_count: str
    retweet_count: str
    created_at: str


class TwitterApi(ApiHandler, ABC):
    """
    Twitter API handler class
    """

    def __init__(self,
                 keyword: str,
                 max_sample_count: int,
                 language: Optional[str] = 'en'):
        self.keyword = keyword
        self.max_sample_count = max_sample_count
        self.language = language

    @staticmethod
    def connection():
        """
        Try to resolve and get Twitter API connection
        """
        try:
            auth = tweepy.OAuthHandler(consumer_key=config.get('twitter', 'consumer_key'),
                                       consumer_secret=config.get('twitter', 'consumer_secret'))
            auth.set_access_token(key=config.get('twitter', 'access_token'),
                                  secret=config.get('twitter', 'access_token_secret'))

            api = tweepy.API(auth)
            api.verify_credentials()

            return api

        except Exception as e:
            print(f"Unable to access Twitter API {e}")

    def iterate(self) -> Iterator[ApiSample]:
        """
        Iterate Tweet samples
        """
        sample_id = 0
        try:
            for tweet in tweepy.Cursor(self.connection().search,
                                       q=self.keyword,
                                       lang=self.language,
                                       count=self.max_sample_count).items():
                yield TwitterSample(
                    text=tweet.text,
                    user_name=tweet.user.name,
                    user_statuses_count=tweet.user.statuses_count,
                    user_followers_count=tweet.user.followers_count,
                    user_location=tweet.user.location,
                    user_verified=tweet.user.verified,
                    favorite_count=tweet.favorite_count,
                    retweet_count=tweet.retweet_count,
                    created_at=tweet.created_at)

                sample_id += 1
                if sample_id >= self.max_sample_count:
                    break

        except Exception as e:
            print(f"Error while iterating Twitter API {e}")

