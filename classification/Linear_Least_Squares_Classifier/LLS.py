#!/usr/bin/env python
from numpy.linalg import inv, solve, matrix_rank
import numpy as np
import sys, os
from random import shuffle, randint


def train(x,y):
	"""
		Build the linear least weight vector W
		:param x: NxD matrix containing N attributes vectors for training
		:param y: NxK matrix containing N class vectors for training
	"""
	# D = Number of attributes
	D = x.shape[1] + 1
	# K = Number of classes
	K = y.shape[1]
	
	# Build the sums of xi*xi' and xi*yi'
	sum1 = np.zeros((D,D)) # init placeholder
	sum2 = np.zeros((D,K))
	i = 0
	for x_i in x:						# loop over all vectors
		x_i = np.append(1, x_i) 		# augment vector with a 1 
		y_i = y[i]						
		sum1 += np.outer(x_i, x_i)		# find xi*xi'
		sum2 += np.outer(x_i, y_i)		# find xi*yi'
		i += 1
	
	# Check that condition number is finite
	# and therefore sum1 is nonsingular (invertable)
	while matrix_rank(sum1) != D:
		# Naive choice of sigma.
		# Could cause inaccuracies when sum1 has small values
		# However, in most cases the matrix WILL be invertable
		sum1 = sum1 + 0.001 * np.eye(D) 
	
	# Return weight vector
	# Weight vector multiplies sums and inverse of sum1
	return np.dot(inv(sum1),sum2)


def predict(W, x):
	"""
	Predict the class y of a single set of attributes
	:param W:	DxK Least squares weight matrix
	:param x:	1xD matrix of attributes for testing
	:return:	List of 0's and 1's. Index with 1 is the class of x
	"""
	x = np.append(1, x)		# augment test vector

	# Solve W'*x
	values = list(np.dot(W.T,x))
	
	# Find maxima of values
	winners = [i for i, x in enumerate(values) if x == max(values)] # indexes of maxima
	# Flip a coin to decide winner
	# if only one winner, it will be chosen by default
	index = randint(0,len(winners)-1)
	winner = winners[index]

	y = [0 for x in values] 	# initalize list with all zeros
	y[winner] = 1 				# set winner
	return y

def fixLabels(y):
	"""
	Fixes labels so they fit our methods
	:param y:	List of numbers cooresponding to class of each
	:return:	Matrix of 0/1 lists.
				Index in list with 1 is class of the cooresponding data
				Example: [0 1 2] => [[1 0 0], [0 1 0], [0 0 1]]
	"""
	newY = []
	for i in range(len(y)):
		# Each list is the size of the largest class number
		size = max(y)
		temp = [0 for j in range(size + 1)]	# initalize list with zeroes
		temp[y[i]] = 1		
		newY.append(temp)	# add to matrix
	return np.matrix(newY)

def test(a,b, split):
	"""
	Runs the linear least squares classifier
	:param a:	All the data
	:param b:	All the classes corresponding to data
	:param split: 	Where to split data for training
					Ex: 40 trains with 40% and tests with 60%
	"""

	# Build weight vector from training data
	W = train(a[:split],b[:split])
	# Build test sets
	x = a[split:]
	y = b[split:]
	
	total = y.shape[0]
	i = 0
	hits = 0
	# Predict the class of each xi, and compare with given class
	for i in range(total):
		prediction = predict(W,x[i])
		actual = list(y[i].A1)
		if prediction == actual:
			hits += 1
	accuracy = hits/float(total)*100
	print ("Accuracy = " + str(accuracy) + "%", "(" + str(hits) + "/" + str(total) + ")")

def usage():
	return 'usage: %s <data file> [head/tail]\n' % os.path.basename( sys.argv[ 0 ] )

def main(path):
	# Check command-line arguments
	if len(sys.argv) < 2:
		print (usage())
		sys.exit(1)
	# The head flag means the class is at the beginning of each line in the data file
	# Default is at the end of each line
	head = False
	if "--head" in sys.argv:
		head = True
	
	data = []
	classes = []
	f = path # open data file
   #f = open("iris.csv")
	try:
		# parse file
		for line in f:
			if line == "\n" or line == "": continue # skip empty lines
			line = line.strip("\n").split(",")		# split line
			if head:
				# Convert raw data to floats and add to data list
				data.append(map(lambda x: float(x), line[0:]))
				# Add class to list
				classes.append(line[0])
			else:
				# Convert raw data to floats and add to data list
				data.append(map(lambda x: float(x), line[:-1]))
				# Add class to list
				classes.append(line[-1])
			
	finally:
		f.close()
	
	# Convert class names to a number
	classes = map(lambda x: list(set(classes)).index(x), classes)
	
	# Final preperations for attributes and classes
	x = np.matrix(data)
	y = fixLabels(classes)


	# shuffle data for better accuracy
	z = [] # temp array
	size = x.shape[0] - 1
	for i in range(size):
		z.append((x[i],y[i]))
	shuffle(z)
	for i in range(size):
		x[i] = z[i][0]
		y[i] = z[i][1]
		
	# scale data so it fits in range (0,1)
	for i in range(size):
		x[i] = x[i] / x.max()
	
	# train and test data
	print ("50% Train/50% Test")
	split = int(size * 0.5)
	test(x,y,split)
	print ("\n")

	print ("40% Train/60% Test")
	split = int(size * 0.4)
	test(x,y,split)
	print ("\n")

	print ("30% Train/70% Test")
	split = int(size * 0.3)
	test(x,y,split)
	print ("\n")

	print ("20% Train/80% Test")
	split = int(size * 0.2)
	test(x,y,split)
	print ("\n")

	print ("10% Train/90% Test")
	split = int(size * 0.1)
	test(x,y,split)

