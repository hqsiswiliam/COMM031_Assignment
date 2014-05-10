import os
import glob

training_filenames_positive = glob.glob("./*.txt")
results = []
for filename in training_filenames_positive:
	file_in_folder = open(filename, 'r')
	filecontents = file_in_folder.readlines()
	for line in filecontents:
		a_line = line.strip('\n')
		a_line = unicode( a_line, "utf-8","ignore" )
		if a_line!='\r':
			results.append(a_line)

# print results
count = 0
for r in results:
	savingPath = './spiltTweets/%d.txt' %(count)
	count = count+1
	file = open(savingPath, "w")
	file.write(r)
	file.close()

strf = './spiltTweets/%d.txt' %(count)
print strf
# f = open('./liverpool2.txt')
# filecontents = f.readlines()
# for line in filecontents:
#   a_line = line.strip('\n')
  # if a_line!='\r':
  # 	results.append(a_line)
# print results


