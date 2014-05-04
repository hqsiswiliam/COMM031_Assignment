import pickle
import os
import glob
#load bayesian classifier
bayesian_classfier = pickle.load(open("bayesian_classfier.ciclass", "rb"))
tfidf = pickle.load(open("tfidf.ciclass", "rb"))

#load the test data
testdata_filename = glob.glob(os.path.join("./test/", '*'))
testdata = []
for filename in testdata_filename:
	#r in here means readonly
	file_obj = open(filename, 'r').read()
	content = unicode( file_obj, "utf-8","ignore" )
	testdata.append(content)

#extract features from test data
test_feature = tfidf.transform(testdata)
#make prediction using classifier
result = bayesian_classfier.predict(test_feature)
print result