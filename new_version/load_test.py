import pickle
import os
import glob
#load bayesian classifier
bayesian_classfier = pickle.load(open("bayesian_classfier.ciclass", "rb"))
tfidf = pickle.load(open("tfidf.ciclass", "rb"))

def predictTheResult(data_set):
	print ('%d data as input' %(len(data_set)))
	test_feature = tfidf.transform(data_set)
	raw_result = bayesian_classfier.predict(test_feature)
	print raw_result
	if len(raw_result)==0:
		return [0,0,0]
	index = 0
	result = [0,0,0]
	for r in raw_result:
		if r== 0:
			result[0] = result[0]+1
		elif r==1:
			result[1] = result[1]+1
		elif r==2:
			result[2] = result[2]+1
	index = 0
	totalRate = 0.0000000000000
	while index <3:
		result[index] = float(result[index])/float(len(raw_result))
		totalRate = totalRate+result[index]
		index = index+1
	print ('total rate: %f'%(totalRate))
	return result


# # load the test data
# testdata_filename = glob.glob("./training_set/general_good/spiltTweets/*")
# testdata = []
# for filename in testdata_filename:
# 	#r in here means readonly
# 	tweet = open(filename, 'r').read()
# 	tweet = unicode( tweet, "utf-8","ignore" )
# 	testdata.append(tweet)
# print len(testdata)
# print predictTheResult(testdata)
# #extract features from test data
# test_feature = tfidf.transform(testdata)
# #make prediction using classifier
# result = bayesian_classfier.predict(test_feature)
# print result