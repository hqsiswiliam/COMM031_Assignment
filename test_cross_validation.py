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
percentage=0.1
step=1000
pattern ='(?u)\\b[A-Za-z]{3,}'
#start to load files
training_set_filename_positive = glob.glob(os.path.join("./testing_ham/", '*'))
training_set_filename_negative = glob.glob(os.path.join("./testing_spam/", '*'))
training_num_of_positive = len(training_set_filename_positive)
training_num_of_negative = len(training_set_filename_negative)
print (training_num_of_positive)
print (training_num_of_negative)
training_set = []
label_set = []
for filename in training_set_filename_positive:
	file_obj = open(filename, 'r').read()
	content = unicode( file_obj, "utf-8","ignore" )
	training_set.append(content)
	label_set.append(1)
for filename in training_set_filename_negative:
	file_obj = open(filename, 'r').read()
	content = unicode( file_obj, "utf-8","ignore" )
	training_set.append(content)
	label_set.append(0)
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
while n<2:
	n=n+1
	print ("Max ngram is %d" % (n))
	classifier = MultinomialNB()
	tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words=None, token_pattern=pattern, ngram_range=(1, n))
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
	pickle.dump(classifier,open("bayesian_classfier.ciclass","wb"))
	pickle.dump(tfidf, open("tfidf.ciclass","wb"))

