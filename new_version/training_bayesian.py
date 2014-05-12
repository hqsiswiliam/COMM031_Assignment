from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import time 
import os
from sklearn.naive_bayes import MultinomialNB
import pickle

#label from 0
training_filenames_positive = glob.glob("./training_set/general_good/spiltTweets/*")
training_filenames_negative = glob.glob("./training_set/general_bad/spiltTweets/*")
training_filenames_neutral = glob.glob("./training_set/Neutral/spiltTweets/*")

#contains both positive and negative data
tweets_data = []
#contains labels corresponding to data
tweets_label = []

for filename in training_filenames_positive:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(0)

for filename in training_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(1)

for filename in training_filenames_neutral:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(2)

#the pattern means search the word which only contains a-z, A-Z, 0-9, and length greater than 1
pattern = '[a-zA-Z0-9#_@%]{1,}'
#set the feature extractor's parameter, in here I set maximum df to 0.9, because tweets is fair more simple than other text.
#also, the ngram is set to 1-3 to enhance the accurancy, make sure all the content convert into lowercase
tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.9, stop_words=None, 
	token_pattern=pattern, ngram_range=(1, 7), lowercase=True)
#do the feature feature extraction
training_feature = tfidf.fit_transform(tweets_data)
print training_feature.shape
#create a Multinomial Bayesian classifer
bayesian_classfier = MultinomialNB() 
#fit the classfier with feature data and its label
bayesian_classfier.fit(training_feature, tweets_label)
#then save the classifer and feature extractor for further use
pickle.dump(bayesian_classfier,open("bayesian_classfier.ciclass","wb"))
pickle.dump(tfidf, open("tfidf.ciclass","wb"))
#do the test
# testdata_filename = glob.glob(os.path.join("./test/", '*'))
# testdata = []
# for filename in testdata_filename:
# 	#r in here means readonly
# 	file_obj = open(filename, 'r').read()
# 	content = unicode(file_obj,"utf-8","ignore")
# 	testdata.append(content)





