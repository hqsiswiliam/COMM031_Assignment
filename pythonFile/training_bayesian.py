from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import time 
import os
from sklearn.naive_bayes import MultinomialNB
import pickle
import cross_validation

#label from 0
training_filenames_positive = glob.glob("Positive_Others/*.txt")
training_filenames_negative = glob.glob("Negative_Others/*.txt")
training_filenames_anger = glob.glob("Anger/*.txt")
training_filenames_happiness = glob.glob("Happiness/*.txt")
training_filenames_neutral = glob.glob("Neutral/*.txt")
training_filenames_sad = glob.glob("Sad/*.txt")

training_number_of_pos = len(training_filenames_positive) 
training_number_of_neg = len(training_filenames_negative)
training_number_of_ang = len(training_filenames_anger) 
training_number_of_hap = len(training_filenames_happiness)
training_number_of_neu = len(training_filenames_neutral) 
training_number_of_sad = len(training_filenames_sad)
#contains both positive and negative data
tweets_data = []
#contains labels corresponding to data
tweets_label = []

for filename in training_filenames_neutral:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(0)

for filename in training_filenames_happiness:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(1)

for filename in training_filenames_positive:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(2)

for filename in training_filenames_anger:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(3)

for filename in training_filenames_sad:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(4)

for filename in training_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	tweets_data.append(tweet)
	tweets_label.append(5)

#the pattern means search the word which only contains a-z, A-Z, 0-9, and length greater than 1
pattern = '[a-zA-Z0-9#_]{1,}'
#set the feature extractor's parameter, in here I set maximum df to 0.7, because tweets is fair more simple than other text.
#also, the ngram is set to 1-3 to enhance the accurancy, make sure all the content convert into lowercase
tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.7, stop_words=None, 
	token_pattern=pattern, ngram_range=(1, 2), lowercase=True)
#do the feature feature extraction
training_feature = tfidf.fit_transform(tweets_data)

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





