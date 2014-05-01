import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = '1y4WdNqMIpNYkAn1nxaXK7eXo'
consumer_secret = ''
access_token = '2231668399-fbqTk5yqUjdA7owjGWL4knuzaW5V5TpklzyL3ag'
access_token_secret = ''
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

results = api.search(q='2012',lang='zh',result_type='mix',count='450')
for result in results:
	print result.text.encode('utf8')