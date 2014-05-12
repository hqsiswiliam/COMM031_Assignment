import tweepy
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import my_api

def createTweepyAPIObject(consumer_key = '43DH3cys1RRfSEJLmnP3S9FYY',consumer_secret = 'zAnNf0Zf0PkpZiz3Dt6g4LDIVV1XlFE8WYPihRewGk0ztP2UIk',
	access_token = '2231668399-D1UMW69W1dVA4eJox8UC5AqdHBzojkk9Z0zp4xR', access_token_secret = 'FNzBjK5uqehbfgM9a93iyRoPtR0uv81suSjL8WYpqRt15'):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	 #create instance
	api = tweepy.API(auth)
	return api
API = createTweepyAPIObject()

#return a list contains trends search query from all over the world
def search_queries_in_trends_world():
	api = API
	trend_place = api.trends_place(1)
	# print trend_place
	i = 0
	queries_list = []
	while i<len(trend_place[0]['trends']):
		temp_query = trend_place[0]['trends'][i]['query']
		queries_list.append(temp_query.encode("UTF8"))
		i=i+1
	return queries_list
#return none, print woeid with location
def print_woeid_location():
	api = API
	# api.trends_woeid()
	trends_available =  api.trends_available()
	woeid_list = []
	i=0
	#################################
	#demostrate woeid representation#
	#################################
	while i < len(trends_available):
		temp_woeid = trends_available[i]['woeid']
		temp_location = trends_available[i]['name']
		woeid_list.append(temp_woeid)
		woeid_list.append(temp_location)
		i=i+1
	i=0
	while i < len(woeid_list):
		print ("woeid: %d Location: %s" % (woeid_list[i], woeid_list[i+1].encode("utf8")))
		i = i+2
		if(i>len(woeid_list)):
			break
	return None

def queries_for_keyword(keyword,count='100'):
	api = API
	raw_result = api.search(q=keyword,lang='en',result_type='mix',count=count)
	result = []
	for r in raw_result:
		result.append(r.text.encode('utf8'))
	return result
print_woeid_location()
world_q = search_queries_in_trends_world()
# print queries_for_keyword(world_q[0])