import tweepy
# Consumer keys and access tokens, used for OAuth
consumer_key = '1y4WdNqMIpNYkAn1nxaXK7eXo'
consumer_secret = '3AeL5gLcjyc6XOrKNQ6e1vIjl5Z9ZiPnaJ1d6kLh2fI4TlDpVi'
access_token = '2231668399-fbqTk5yqUjdA7owjGWL4knuzaW5V5TpklzyL3ag'
access_token_secret = 'UOg11BiALpTsAn74r0JBgkOtiRamVtJ6idmLqctZHOxKQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)


results = api.search(q='Ukraine',lang='en',result_type='mix',count='100')


file = open("Ukraine.txt", "w")
for result in results:
	# print result.text.encode('utf8')
	# print '\n'
	file.write(result.text.encode('utf8'))
	file.write('\n\n')
file.close()

print ("Count: %d" % len(results))
print 'DONE!!!!'