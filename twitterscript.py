# Import the necessary package to process data in JSON format
import OSC

try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

with open('secret.txt') as f:
    content = f.readlines()

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = content[0].rstrip("\r\n")
ACCESS_SECRET = content[1].rstrip("\r\n")
CONSUMER_KEY = content[2].rstrip("\r\n")
CONSUMER_SECRET = content[3].rstrip("\r\n")

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="Trump", language="en")


c = OSC.OSCClient()
c.connect(('127.0.0.1', 6448))   # localhost, port 57120
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/wek/inputs")

trumpTags = 0
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    try:
        for hashtag in tweet['entities']['hashtags']:
            text = json.dumps(hashtag['text']).lower()
            if ("trump" in text):
                trumpTags += 1
    except:
    # read in a line is not in JSON format (sometimes error occured)
        continue  

    if (tweet_count % 10 == 0):
        trumpTags = 0

    oscmsg.append(float(trumpTags)/10)
    print oscmsg
    c.send(oscmsg)
    oscmsg.clearData()
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break