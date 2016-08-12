import sys
import operator
import requests
import json
import twitter

def analyze(handle):

#Insert your Twitter dev account info here
    	twitter_consumer_key = ''
    	twitter_consumer_secret = ''
    	twitter_access_token = ''
    	twitter_access_secret = ''

    	twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=twitter_access_token,
                      access_token_secret=twitter_access_secret)
    	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
    	text = ""
    	for s in statuses:
    	    if (s.lang =='en'):
        			text += s.text.encode('utf-8')
            text += "\n\n"
	return text

#Insert desired Twitter handle here
user_handle = "@Github"
user_result = analyze(user_handle)

#Spits out the last 200 Statuses to Output.txt
text_file = open("Output.txt", "w")
text_file.write(user_result)
text_file.close()
