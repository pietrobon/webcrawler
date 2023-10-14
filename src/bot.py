import os
import tweepy
from dotenv import load_dotenv

class BOT:

    def __init__(self):
        load_dotenv()
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_key_secret = os.getenv('CONSUMER_KEY_SECRET')

        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

        bearer_token = os.getenv('BEARER_TOKEN')

        self.client = tweepy.Client(
            consumer_key=consumer_key,
            consumer_secret=consumer_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            bearer_token=bearer_token
        )
        #Use this option only if you need to attach an image to the post
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_key_secret)
        auth.set_access_token(
            access_token,
            access_token_secret
        )

        self.api = tweepy.API(auth)

    def post(self, data: dict):
        try:

            post = "{}\n\nCotação Atual: R$ {}".format(
                data["currency"],
                data["cost"].replace('.', ',')
            )
            self.client.create_tweet(text=post)
            return True
        except Exception as e:
            print(f"Failed to post: {e}")
