from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_analysis as s

from twitterkeys improt *

class listner(StreamListener):
    
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence >= 0.80:
            file = open('twitter-output.txt', 'a')
            file.write(sentiment_value)
            file.write('\n')
            file.close()
        
    def on_error(self, status):
        print(status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listner())
twitterStream.filter(track = ['Hollywood'])