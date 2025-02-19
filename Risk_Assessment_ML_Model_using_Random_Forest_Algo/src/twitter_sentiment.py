import tweepy
import os
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def analyze_twitter(username):
    try:
        user = client.get_user(username=username, user_fields=["id"])
        user_id = user.data.id

        tweets = client.get_users_tweets(id=user_id, max_results=10, tweet_fields=["text"])

        if not tweets.data:
            return 500  

        sentiments = [TextBlob(tweet.text).sentiment.polarity for tweet in tweets.data]
        avg_sentiment = sum(sentiments) / len(sentiments)

        social_credit_score = int(300 + ((avg_sentiment + 1) / 2) * 600)

        return social_credit_score

    except tweepy.errors.TweepyException as e:
        print(f"Twitter API Error: {e}")
        return 500  

if __name__ == "__main__":
    print("Social Media Score : ")
    print(analyze_twitter("elonmusk"))
