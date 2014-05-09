from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer

def test():
		print 'Pass test!'
		return None
#do the cross-validation, in here, vector should be shape as (2, n)
#we compare the correctness for Guassian Bayesian, Multinomial Bayesian, and Bernoulli Bayesian
def spilteDataAndLabel(training_set,label_set,count,percentage,step=1):
	# sliced_training_data
	# sliced_testing_data
	# sliced_training_label
	# sliced_testing_label
	size_training_set = len(training_set)
	
	if(size_training_set!=len(label_set)):
			return None, None, None, None
	#start to slice training_set
	#in case of indexTo bigger than size of the training set
	doubled_training_set = training_set+training_set
	#indexes for slice of training data
	indexFrom = int((count*step)%size_training_set)
	indexTo = int(indexFrom+(percentage*size_training_set))
	sliced_testing_data = doubled_training_set[indexFrom:indexTo]
	#slicing training data
	if indexTo>size_training_set:
			sliced_training_data = training_set[indexTo-size_training_set:indexTo]
	else:
			temp1 = training_set[0:indexFrom]
			temp2 = training_set[indexTo:size_training_set]
			sliced_training_data = temp1+temp2

	#now slice label_set
	doubled_label_set = label_set+label_set
	sliced_testing_label = doubled_label_set[indexFrom:indexTo]
	#slicing training data
	if indexTo>size_training_set:
			sliced_training_label = label_set[indexTo-size_training_set:indexTo]
	else:
			temp1 = label_set[0:indexFrom]
			temp2 = label_set[indexTo:size_training_set]
			sliced_training_label = temp1+temp2
	#return sliced training_set and label_set
	return sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label


################################################
#																							 #
#   FOLLOWING METHODS ARE ABANDONED            #
#		BECAUSE OF SOME UNKNOWN ERRORS 						 #
#																							 #
################################################	
def multinomial_cross_validation(training_set, label_set, percentage=0.1,step=1, pattern ='(?u)\\b[A-Za-z]{3,}'):
	classifier = MultinomialNB()
	tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.9, stop_words=None, 
	token_pattern=pattern, ngram_range=(1, 3))
# 	total_testing_times = 0;
# 	error_testing_times = 0;
# 	size_training_set = len(training_set)
# 	total_num_loop = int(size_training_set/step)
# 	x = 0
# 	print ("There are %d loops" % (total_num_loop))
# 	while x<total_num_loop:
# 		x = x+1
# 		print ("This is %d loop" % (x))
# 		#start to slice array and train classifer
# 		[sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=spilteDataAndLabel(
# 			training_set,label_set,x,percentage,step=step)
# 		training_feature = tfidf.fit_transform(sliced_training_data)
# 		classifier.fit(training_feature, sliced_training_label)
# 		#start to testing
# 		indexOfTest = 0
# 		testing_feature = tfidf.transform(sliced_testing_data)
# 		test_result = classifier.predict(testing_feature)
		
# 		while indexOfTest < len(sliced_testing_data):
# 			total_testing_times = total_testing_times+1
# 			if test_result[indexOfTest]!=sliced_testing_label[indexOfTest]:
# 				error_testing_times = error_testing_times+1
# 			indexOfTest=indexOfTest+1
# 	successRatio =1-float(error_testing_times)/float(total_testing_times)
# 	return successRatio

# #GaussianNB 
# def gaussian_cross_validation(training_set, label_set, percentage=0.1,step=1, pattern ='(?u)\\b[A-Za-z]{3,}'):
# 	classifier = GaussianNB()
# 	tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.9, stop_words=None, 
# 	token_pattern=pattern, ngram_range=(1, 3))
# 	total_testing_times = 0;
# 	error_testing_times = 0;
# 	size_training_set = len(training_set)
# 	total_num_loop = int(size_training_set/step)
# 	x = 0
# 	print ("There are %d loops" % (total_num_loop))
# 	while x<total_num_loop:
# 		x = x+1
# 		print ("This is %d loop" % (x))
# 		#start to slice array and train classifer
# 		[sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=spilteDataAndLabel(
# 			training_set,label_set,x,percentage,step=step)
# 		training_feature = tfidf.fit_transform(sliced_training_data)
# 		classifier.fit(training_feature, sliced_training_label)
# 		#start to testing
# 		indexOfTest = 0
# 		testing_feature = tfidf.transform(sliced_testing_data)
# 		test_result = classifier.predict(testing_feature)
		
# 		while indexOfTest < len(sliced_testing_data):
# 			total_testing_times = total_testing_times+1
# 			if test_result[indexOfTest]!=sliced_testing_label[indexOfTest]:
# 				error_testing_times = error_testing_times+1
# 			indexOfTest=indexOfTest+1
# 	successRatio =1-float(error_testing_times)/float(total_testing_times)
# 	return successRatio

# #BernoulliNB
# def bernoulli_cross_validation(training_set, label_set, percentage=0.1,step=1, pattern ='(?u)\\b[A-Za-z]{3,}'):
# 	classifier = BernoulliNB()
# 	tfidf = TfidfVectorizer(sublinear_tf=True, max_df=0.9, stop_words=None, 
# 	token_pattern=pattern, ngram_range=(1, 3))
# 	total_testing_times = 0;
# 	error_testing_times = 0;
# 	size_training_set = len(training_set)
# 	total_num_loop = int(size_training_set/step)
# 	x = 0
# 	print ("There are %d loops" % (total_num_loop))
# 	while x<total_num_loop:
# 		x = x+1
# 		print ("This is %d loop" % (x))
# 		#start to slice array and train classifer
# 		[sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=spilteDataAndLabel(
# 			training_set,label_set,x,percentage,step=step)
# 		training_feature = tfidf.fit_transform(sliced_training_data)
# 		classifier.fit(training_feature, sliced_training_label)
# 		#start to testing
# 		indexOfTest = 0
# 		testing_feature = tfidf.transform(sliced_testing_data)
# 		test_result = classifier.predict(testing_feature)
		
# 		while indexOfTest < len(sliced_testing_data):
# 			total_testing_times = total_testing_times+1
# 			if test_result[indexOfTest]!=sliced_testing_label[indexOfTest]:
# 				error_testing_times = error_testing_times+1
# 			indexOfTest=indexOfTest+1
# 	successRatio =1-float(error_testing_times)/float(total_testing_times)
# 	return successRatio



