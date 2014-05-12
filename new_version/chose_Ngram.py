import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import time 
import os
import helper_cross_validation
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
helper_cross_validation.test()
max_ngram = 15
percentage=0.02
step=65
pattern = '[a-zA-Z0-9#_@%]{1,}'
#start to load files
training_filenames_positive = glob.glob("./training_set/general_good/spiltTweets/*.txt")
training_filenames_negative = glob.glob("./training_set/general_bad/spiltTweets/*.txt")
training_filenames_neutral = glob.glob("./training_set/Neutral/spiltTweets/*.txt")
training_number_of_pos = len(training_filenames_positive) 
training_number_of_neg = len(training_filenames_negative)
training_number_of_neu = len(training_filenames_neutral) 
total_size = training_number_of_pos+training_number_of_neg+training_number_of_neu
print total_size
training_set = []
label_set = []
for filename in training_filenames_positive:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	training_set.append(tweet)
	label_set.append(0)

for filename in training_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	training_set.append(tweet)
	label_set.append(1)

for filename in training_filenames_neutral:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	training_set.append(tweet)
	label_set.append(2)

#end of loading files
################################################
#																							 #
#   NOW STARTING TO DO CROSSVALIDATION         #
#		FOR MULTINOMIAL BAYESIAN									 #
#																							 #
################################################	
#TO DETERMINE THE BEST NGRAM
print "This is for max_df parameter"
n=0
while n<max_ngram:
	n=n+1
	print ("Max ngram is %d" % (n))
	classifier = MultinomialNB()
	tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.9, stop_words=None, token_pattern=pattern, ngram_range=(1, n))
	total_testing_times = 0;
	error_testing_times = 0;
	size_training_set = len(training_set)
	total_num_loop = int(size_training_set/step)
	x = 0
	# print ("There are %d loops" % (total_num_loop))
	while x<total_num_loop:
		x = x+1
		# print ("This is %d loop" % (x))
		#start to slice array and train classifer
		[sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=helper_cross_validation.spilteDataAndLabel(
			training_set,label_set,x,percentage,step=step)
		training_feature = tfidf.fit_transform(sliced_training_data)
		classifier.fit(training_feature, sliced_training_label)
		#start to testing
		indexOfTest = 0
		testing_feature = tfidf.transform(sliced_testing_data)
		test_result = classifier.predict(testing_feature)
		
		while indexOfTest < len(sliced_testing_data):
			total_testing_times = total_testing_times+1
			if test_result[indexOfTest]!=sliced_testing_label[indexOfTest]:
				error_testing_times = error_testing_times+1
			indexOfTest=indexOfTest+1
	successRatio =1-float(error_testing_times)/float(total_testing_times)
	print ("Success Ratio is %f" % (successRatio))

