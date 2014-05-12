from sklearn.feature_extraction.text import TfidfVectorizer
import glob
import numpy as np
from ffnet import ffnet, tmlgraph
import helper_cross_validation
import random
import math
percentage=0.05
step=65
#read the training filenames
training_filenames_positive = glob.glob("./training_set/general_good/spiltTweets/*.txt")
training_filenames_negative = glob.glob("./training_set/general_bad/spiltTweets/*.txt")
training_filenames_neutral = glob.glob("./training_set/Neutral/spiltTweets/*.txt")


#create empty data holders
raw_data = []
raw_labels = []

for filename in training_filenames_positive:
  #read the actual tweets
  tweet = open(filename, 'r').read()
  tweet = unicode( tweet, "utf-8","ignore" )
  raw_data.append(tweet)
  raw_labels.append(0)

for filename in training_filenames_negative:
  #read the actual tweets
  tweet = open(filename, 'r').read()
  tweet = unicode( tweet, "utf-8","ignore" )
  raw_data.append(tweet)
  raw_labels.append(1)

for filename in training_filenames_neutral:
  #read the actual tweets
  tweet = open(filename, 'r').read()
  tweet = unicode( tweet, "utf-8","ignore" )
  raw_data.append(tweet)
  raw_labels.append(2)

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 6),token_pattern=ur'\b\w+\b',min_df=0.05)
tfidf_vectorizer.fit(raw_data)
feature_names = tfidf_vectorizer.get_feature_names()


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

def annealingSimulation(data_s,data_l,max_nodes,min_nodes,temperature=10000.0,cool=0.15,step=10):
  #generate a random number to start
  if min_nodes<0:
  	min_nodes=0
  initial_random_number = random.randint(min_nodes,max_nodes)
  nodeA = initial_random_number
  while temperature>0.1:
    direction = random.randint(-step,step)
    nodeB = nodeA+direction
    if nodeB>max_nodes:
      nodeB = max_nodes
    elif nodeB<min_nodes:
      nodeB = min_nodes
    #start to do the cross validation for number of nodeA
    percentage = 0.05
    size_training_set = len(data_s)
    total_num_loop = 1
    x = 0
    total_num = 0
    total_error = 0
    while x<total_num_loop:
      x=x+1
      #start to create net classifier
      print 'start to create NN'
      print ('Hidden nodeA are %d' %(nodeA))
      [sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=helper_cross_validation.spilteDataAndLabel(data_s,data_l,x,percentage,step=len(data_s))
      [net,number_of_input_features,tfidf_vectorizer] = creatingNeuralNetwork(nodeA,sliced_training_data,sliced_training_label)
      #start to testing
      indata = np.zeros((len(sliced_testing_data),number_of_input_features))
      for j,sentence in enumerate(sliced_testing_data):
        indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]
      #testing the result 
      results = net(indata)
      results_list = []
      for r in results:
        if r<0.5:
          r=0
        elif r>=0.5 and r <1.5:
          r=1
        elif r>=1.5:
          r=2
        results_list.append(r)
      total_num = total_num+len(results_list)
      index = 0
      while index < len(results_list):
        if results_list[index]!=sliced_testing_label[index]:
          total_error = total_error+1
        index = index+1
    error_rateA = float(total_error)/float(total_num)


    #cross validation for nodeB
    percentage = 0.02
    size_training_set = len(data_s)
    #too much time occupied
    total_num_loop = 1
    x = 0
    total_num = 0
    total_error = 0
    while x<total_num_loop:
      x=x+1
      #start to create net classifier
      [sliced_training_data,sliced_testing_data,sliced_training_label,sliced_testing_label]=helper_cross_validation.spilteDataAndLabel(data_s,data_l,x,percentage,step=len(data_s))
      print 'start to create NN'
      print ('Hidden nodeB are %d' %(nodeB))
      [net,number_of_input_features,tfidf_vectorizer] = creatingNeuralNetwork(nodeB,sliced_training_data,sliced_training_label)
      #start to testing
      indata = np.zeros((len(sliced_testing_data),number_of_input_features))
      for j,sentence in enumerate(sliced_testing_data):
          indata[j,:] =  tfidf_vectorizer.transform([sentence]).toarray()[0]
      #testing the result 
      results = net(indata)
      results_list = []
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
        results_list.append(r)
      total_num = total_num+len(results_list)
      index = 0
      while index < len(results_list):
        if results_list[index]!=sliced_testing_label[index]:
          total_error = total_error+1
        index = index+1
    error_rateB = float(total_error)/float(total_num)
    p=pow(math.e,(-error_rateB-error_rateA)/temperature)
    if (error_rateB<error_rateA or random.random()<p):
      nodeA=nodeB
      print ("Node number: %d, accurancy: %f" %(nodeB,1-error_rateB)) 
    else:
       print ("Node number: %d, accurancy: %f" %(nodeA,1-error_rateA)) 
    #cooling a little bit
    temperature=temperature*cool
  return nodeA

#chose the hidden node from 0-1500
num = annealingSimulation(raw_data,raw_labels,50,1,step=1)

print ("best node is %d" %(num))