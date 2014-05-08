import tweepy
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# Consumer keys and access tokens, used for OAuth
consumer_key = '1y4WdNqMIpNYkAn1nxaXK7eXo'
consumer_secret = '3AeL5gLcjyc6XOrKNQ6e1vIjl5Z9ZiPnaJ1d6kLh2fI4TlDpVi'
access_token = '2231668399-fbqTk5yqUjdA7owjGWL4knuzaW5V5TpklzyL3ag'
access_token_secret = 'UOg11BiALpTsAn74r0JBgkOtiRamVtJ6idmLqctZHOxKQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)

tweets = api.search(q='Master',lang='en',result_type='mix',count='100')
results = []
for result in tweets:
	results.append(result.text.encode('utf8'))

bayesian_classfier = pickle.load(open("bayesian_classfier.ciclass", "rb"))
tfidf = pickle.load(open("tfidf.ciclass", "rb"))
feature_of_tweets = tfidf.transform(results)
result_labels = bayesian_classfier.predict(feature_of_tweets)
positive = 0;
total = len(result_labels)
for i in result_labels:
	if i==1:
		positive = positive+1

ratio_pos = float(positive)/float(total)
print ratio_pos
