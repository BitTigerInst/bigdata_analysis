import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import io
import json
import re
import codecs

ckey = 'f8o7joOytUdranNFjxZr5AWAv'
csecret = 'Iqj5OLu39znMUWeCnReikegyW3G3CEcgCEqg5GzvkY1fAH0v7o'
atoken = '4921648707-6uMJ8itn4DDre6yeiG6f4uhS5zB2voZ1F5p4Zhc'
asecret = 'laIi2r0XDtTIBJR5mqXmghQ8yBauQ5yg2iGRDE0sT7YnI'

start_time = time.time() #grabs the system time
keyword_list = ['ibm,google,amazon,facebook,bloomberg']

filesave = {'ibm': [],
			'google': [],
			'amazon': [],
			'facebook': [],
			'bloomberg': []}

class listener(StreamListener):

	def __init__(self, start_time, time_limit=20):
		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, raw_data):
		if time.time()-start_time>self.limit:
			for keywords in keyword_list[0].split(','):
				with codecs.open('/Users/yibeihuang/Desktop/Se2-Resources/BigData/HW/tweefile/'+keywords+'.txt', 'a', 'utf-8') as f:
					for lines in filesave[keywords]:
						f.write(lines + '\n')
			print 'Finished'
			raw_input('Ctrl-C to exit...')
		data = json.loads(raw_data)
		if 'text' in data:
			for keywords in keyword_list[0].split(','):
				if re.search(keywords, data['text'], re.IGNORECASE):
					filesave[keywords].append(data['text'])

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener(start_time, time_limit=1800))
twitterStream.filter(track=keyword_list, languages=['en'])














