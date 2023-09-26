import tweepy
from django.conf import settings

# Set your API keys and access tokens
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
access_token = settings.ACCESS_TOKEN
access_token_secret = settings.ACCESS_TOKEN_SECRET

def print_key():
    print(f"Consumer Key: {consumer_key}")
    print(f"Consumer Secret: {consumer_secret}")


class TwitterConnector(object):
    def __init__(self, username):
        self.username = username

    def run(self):
        self.__authenticate_to_twitter()
        self.__onboard_a_twitter_profile()

    def __authenticate_to_twitter(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
        
    
    def __onboard_a_twitter_profile(self):
        api = self.__authenticate_to_twitter()
        user = api.get_user(screen_name=self.username)


        twitter_user_object = {
            "twitter_id": user.id_str,
            "twitter_name": user.name,
            "twitter_screen_name": user.screen_name,
            "twitter_user_description": user.description,
            "followers_count": user.followers_count,
            "following_count": user.friends_count,
            "tweets_count": user.statuses_count,
            "location": user.location,
            "twitter_profile_photo": user.profile_image_url
        }  
        print(twitter_user_object) 

