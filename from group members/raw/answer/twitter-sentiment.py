from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import time 

#read the training filenames
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

#create empty data holders
dataset_data = []
dataset_labels = []

#add the tweets to the dataset
for filename in training_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(0)

for filename in training_filenames_positive:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(1)

for filename in training_filenames_anger:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(2)

for filename in training_filenames_happiness:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(3)

for filename in training_filenames_neutral:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(4)

for filename in training_filenames_sad:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	dataset_data.append(tweet)
	dataset_labels.append(5)
	

print 'Extracting the bag of 6-grams vocabulary from the corpus' 
#create the gab of 6-grams vocabulary
t0 = time.time()
tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 6),token_pattern=ur'\b\w+\b',min_df=0.15)
tfidf_vectorizer.fit(dataset_data)
feature_names = tfidf_vectorizer.get_feature_names()
t1 = time.time()
tfidf_time = t1-t0
print 'Time it took to build the bag of 6-grams dictionary: ' + str(tfidf_time) + ' seconds.' 

print len(feature_names)
print feature_names


number_of_input_features = len(feature_names)

# Create the feature dataset
indata = np.zeros((len(dataset_data),number_of_input_features))

for j,sentence in enumerate(dataset_data):
    indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]

print 'Creating the neural network object' 
t2 = time.time()
#create the neural network
number_of_hidden_nodes = number_of_input_features
conec = tmlgraph((number_of_input_features,number_of_hidden_nodes, 1))
net = ffnet(conec)
t3 = time.time()
nn_create_time = t3-t2
print 'Time it took to create the neural network: ' + str(nn_create_time) + ' seconds.' 

print 'Starting the training of the neural network. This will take a while...' 
t4 = time.time()
net.train_tnc(indata, dataset_labels, maxfun = 5000, messages=1) 
t5 = time.time()
nn_train_time = t5-t4
output, regression = net.test(indata, dataset_labels, iprint = 2)
print 'Time it took to train the neural network: ' + str(nn_train_time) + ' seconds.' 

#build the evaluation dataset - similar as above
evaluation_filenames_positive = glob.glob("testing/pos/*.txt")
evaluation_filenames_negative = glob.glob("testing/neg/*.txt")
evaluation_filenames_anger = glob.glob("testing/ang/*.txt")
evaluation_filenames_sad = glob.glob("testing/sad/*.txt")
evaluation_filenames_neutral = glob.glob("testing/neu/*.txt")
evaluation_filenames_happiness = glob.glob("testing/hap/*.txt")
evaluation_number_of_pos = len(evaluation_filenames_positive) 
evaluation_number_of_neg = len(evaluation_filenames_negative)
evaluation_number_of_ang = len(evaluation_filenames_anger) 
evaluation_number_of_sad = len(evaluation_filenames_sad)
evaluation_number_of_neu = len(evaluation_filenames_neutral) 
evaluation_number_of_hap = len(evaluation_filenames_happiness)
print evaluation_number_of_pos
print evaluation_number_of_neg
print evaluation_number_of_ang
print evaluation_number_of_sad
print evaluation_number_of_neu
print evaluation_number_of_hap

evaluation__dataset_data = []
evaluation_dataset_labels = []

for filename in evaluation_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(0)


for filename in evaluation_filenames_positive:
	#read the actual tweet
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(1)

for filename in evaluation_filenames_anger:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(2)


for filename in evaluation_filenames_happiness:
	#read the actual tweet
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(3)
	


for filename in evaluation_filenames_neutral:
	#read the actual tweet
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(4)

	
for filename in evaluation_filenames_sad:
	#read the actual tweet
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	evaluation__dataset_data.append(tweet)
	evaluation_dataset_labels.append(5)
	
# Create train samples
indata = np.zeros((len(evaluation__dataset_data),number_of_input_features))
for j,sentence in enumerate(evaluation__dataset_data):
    indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]

results = net(indata)

print '********************************'
print 'NN Results in evaluation dataset'
print results
print '********************************\n'

print '********************************'
print 'Ground truth for valuation dataset'
print evaluation_dataset_labels
print '********************************\n'
