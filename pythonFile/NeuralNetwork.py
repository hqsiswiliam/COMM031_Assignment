from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import time 
import helper_cross_validation
percentage=0.05
step=65
#read the training filenames
training_filenames_positive = glob.glob("./training_set/Positive_Others/spiltTweets/*.txt")
training_filenames_negative = glob.glob("./training_set/Negative_Others/spiltTweets/*.txt")
training_filenames_anger = glob.glob("./training_set/Anger/spiltTweets/*.txt")
training_filenames_happiness = glob.glob("./training_set/Happiness/spiltTweets/*.txt")
training_filenames_neutral = glob.glob("./training_set/Neutral/spiltTweets/*.txt")
training_filenames_sad = glob.glob("./training_set/Sad/spiltTweets/*.txt")

training_number_of_pos = len(training_filenames_positive) 
training_number_of_neg = len(training_filenames_negative)
training_number_of_ang = len(training_filenames_anger) 
training_number_of_hap = len(training_filenames_happiness)
training_number_of_neu = len(training_filenames_neutral) 
training_number_of_sad = len(training_filenames_sad)

#create empty data holders
raw_data = []
raw_labels = []

for filename in training_filenames_neutral:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(0)

for filename in training_filenames_happiness:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(1)

for filename in training_filenames_positive:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(2)

for filename in training_filenames_anger:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(3)

for filename in training_filenames_sad:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(4)

for filename in training_filenames_negative:
	#read the actual tweets
	tweet = open(filename, 'r').read()
	tweet = unicode( tweet, "utf-8","ignore" )
	raw_data.append(tweet)
	raw_labels.append(5)
	


def creatingNeuralNetwork(num_hidden,data_s,data_l):
  dataset_data = data_s
  dataset_labels = data_l
  #create the gab of 6-grams vocabulary
  tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 6),token_pattern=ur'\b\w+\b',min_df=0.05)
  tfidf_vectorizer.fit(dataset_data)
  feature_names = tfidf_vectorizer.get_feature_names()
  number_of_input_features = len(feature_names)
  # Create the feature dataset
  indata = np.zeros((len(dataset_data),number_of_input_features))
  for j,sentence in enumerate(dataset_data):
    indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]
  #create the neural network
  number_of_hidden_nodes = num_hidden
  conec = tmlgraph((number_of_input_features,number_of_hidden_nodes, 1))
  net = ffnet(conec)
  #please print nothing
  net.train_tnc(indata, dataset_labels, maxfun = 5000, messages=0) 
  output, regression = net.test(indata, dataset_labels, iprint = 0)
  return net, number_of_input_features, tfidf_vectorizer

[net,number_of_input_features,tfidf_vectorizer] = creatingNeuralNetwork(2,raw_data,raw_labels)
# def annealingSimulation(max_nodes,min_nodes,temperature=10000.0,cool=0.95,step=5):
# 	#generate a random number to start
# 	initial_random_number = random.randint(min_nodes,max_nodes)
# 	while temperature>0.1:
# 		direction = random.randint(-step,step)
# 		nodeA = initial_random_number
# 		nodeB = nodeA+direction
# 		if nodeB>max_node:
# 			nodeB = max_nodes
# 		else if nodeB<min_nodes:
# 			nodeB = min_nodes
# 	#create training and testing data set from raw_data and raw_labels

  

evaluation__dataset_data = raw_data
evaluation_dataset_labels = raw_labels


# Create train samples
#extract data
indata = np.zeros((len(evaluation__dataset_data),number_of_input_features))
for j,sentence in enumerate(evaluation__dataset_data):
    indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]
#testing the result 
results = net(indata)

print '********************************'
print 'NN Results in evaluation dataset'
new_r = []
# print results
for r in results:
	if r<0.5:
		r=0
	elif r>=0.5 and r <1.5:
		r=1
	elif r>=1.5 and r<2.5:
		r=2
	elif r>=2.5 and r<3.5:
		r=3
	elif r>=3.5 and r<4.5:
		r=4
	else:
		r=5
	new_r.append(r)

print new_r
print '********************************\n'

print '********************************'
print 'Ground truth for valuation dataset'
print evaluation_dataset_labels
print '********************************\n'

