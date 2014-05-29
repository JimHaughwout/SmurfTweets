import tweepy

consumer_key = 'KBpRsBvL7jyByg9VY48iUxNP2'
consumer_secret = '16F7cBT11aLnT6dacxH8vCeyPW1ugmtBUwOl5S7iMIRGDYwdfS'
access_token = '16373526-MNcmkFIWFAT65fcCBl6P9QVlZQ3hE9TNITAsaXGOO'
access_token_secret = 'cEGAV4QOwhYPOUFfUpPX1t7hmYC8igaGotyzD9qcbqjtK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#my_tweets = api.user_timeline(id = "JHaughwout")
#for tweet in my_tweets:
#    print tweet.text

my_mentions = api.mentions_timeline(id = "JHaughwout")
for tweet in my_mentions:
	#print tweet.author
	print tweet.created_at, "|", tweet.author.screen_name, "|", tweet.author.location, "|", tweet.text

#for status in Cursor(api.user_timeline).items(5):
#    process_status(status)

#for status in Cursor(api.user_timeline, id = "JHaughwout").items():
#	print status