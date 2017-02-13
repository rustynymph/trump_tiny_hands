# Trump Tiny Hands
A custom feature extractor for interactive machine learning that counts up how many trump "hashtags" are occurring every 10 tweets and uses it to shrink Trump's already tiny hands the fewer references he has.  

Follow this guide to getting started using the Twitter API. You will have to follow a few steps to make a Twitter account and also to make a Twitter App that will allow you to authenticate any calls to its API.  
http://socialmedia-class.org/twittertutorial.html

When you are finished, make a file called "secret.txt" in the same directory as the twitterscript.py. Here you will put your keys and tokens, do *not* put them directly into your file if you plan on making it public. It is a security risk and will allow anyone to make API calls from your account.

Your file should contain 4 lines with information in this order:  
ACCESS_TOKEN  
ACCESS_SECRET  
CONSUMER_KEY  
CONSUMER_SECRET  
  
Again, follow the guide above to get these values.  

To run you will need python 2.7.*, and use python's pip package installer to install the Twitter API module.  
`pip install twitter`  

Simply run the python script through the command line (make sure you have internet access)  
`python twitterscript.py`  

The script will send 1 message to wekinator on port 6448 with the address '/wek/inputs'. The processing sketch I've included listens for 1 output with the address '/wek/outputs' on port 12000.

Enjoy!