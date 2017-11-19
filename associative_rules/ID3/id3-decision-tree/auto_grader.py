import random
from modules.ID3 import *
from modules.parse import *
from modules.pruning import *
from modules.graph import *
from modules.predictions import *
from modules.pickled import *

EPSILON = 0.001

## Running File
#
# To run this file select either True or False for each of the options input
# This will use the function found in ID3 or pruning to run the tests and let you know how your algorithm performed.
# If there is an error or a test has been failed please look over your algorithm and try again.
#
options = {
	'homogenous': True,
	'gain_ratio_numeric': True,
	'split_on_nominal': True,
    'split_on_numerical': True,
    'p_best_attribute': True,
    'mode': True,
    'entropy': True,
    'gain_ratio_nominal':True,
    'classify': True
}

def grader(homogenous=False,p_best_attribute=False,mode=False,entropy=False,gain_ratio_nominal=False,split_on_nominal=False,split_on_numerical=False, gain_ratio_numeric=False, classify=False):
	title = "=========="
	gain_ratio_result = True
	if homogenous:
		name = "homogenous"
		print title,name,title
		total = 0
		data_set = [[[0],[1],[1],[1],[1],[1]],[[0],[1],[None],[0]],[[1],[1],[1],[1],[1],[1]]]
		result = [None,None,1]
		for i in xrange(3):
			if check_homogenous(data_set[i]) == result[i]:
				total += 1
				print "Passed %d"%(i+1)
			else:
				print "Failed %d"%(i+1)
		print "Not all tests were met please look at %s"%name if total != 3 else "All tests passed"
	if p_best_attribute:
		name = "pick_best_attribute"
		print title,name,title
		numerical_splits_count = [[20,20],[20,20],[20,20,20,20],[20,20,20,20]]
		a_meta = [[{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
		,[{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}],
                 [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "attitude", 'is_nominal': False}],
                 [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "attitude", 'is_nominal': False}]]
		d_set = [[[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]],
		[[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]],
                [[0, 0, 0.1], [1, 0, 0.2], [0, 2, 0.2], [0, 2, 0.2], [0, 3, 0.1], [1, 1, 0.1], [0, 4, 0.1], [0, 2, 0.1], [1, 2, 0.1], [1, 5, 0.1]],
                [[0, 0, 0.1], [1, 0, 0.2], [0, 2, 0.05], [0, 2, 0.14], [0, 3, 0.3], [1, 1, 0.3], [0, 4, 0.1], [0, 2, 0.1], [1, 2, 0.29], [1, 5, 0.5]] ]
		result = [(1, 0.51),(1, False),(1,False),(2, 0.2)]
		total = 0
		for i in xrange(4):
			if pick_best_attribute(d_set[i], a_meta[i], numerical_splits_count[i]) == result[i]:
				total += 1
				print "Passed %d"%(i+1)
			else:
				print "Failed %d"%(i+1)
		print "Not all tests were met please look at %s"%name if total != 4 else "All tests passed"
	if mode:
		name = "mode"
		print title,name,title
		check_mode()
	if entropy:
		name = "entropy"
		print title,name,title
		check_entropy()
	if gain_ratio_nominal:
		name = "gain_ratio_nominal"
		print title,name,title
		check_gain_ratio_nom()
	if gain_ratio_numeric:
		name = "gain_ratio_numeric"
		print title,name,title
		check_gain_ratio_num()
	if split_on_nominal:
		name = "split_on_nominal"
		print title,name,title
		check_split_on_nominal()
	if split_on_numerical:
		name = "split_on_numerical"
		print title,name,title
		print "Not all tests were met please look at %s"%name if split_o_num(name) is not 2 else "All tests passed"
	if classify:
		name = "classify"
		print title,name,title
		check_classify()
        if ID3:
		name = "ID3"
		print title,name,title
		check_ID3()

def create_data_set(typ):
	return [[random.randint(0,1) if y is 0 else (round(random.random(),2) if typ is 'numeric' else random.randint(0,
		5)) for y in xrange(2)] for x in xrange(10)]

def split_o_num(name):
	sval = [0.48,0.17]
	d_set = [[[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]]]
	d_set.append([[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]])
	result = [([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])]
	result.append(([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]]))
	total = 0
	for i in xrange(2):
		if split_on_numerical(d_set[i],1,sval[i]) == result[i]:
			print "Passed %d"%(i+1)
			total += 1
		else:
			print "Failed %d"%(i+1)
	return total

def check_mode():
	data_set = [[[0],[1],[1],[1],[1],[1]],[[0],[1],[0],[0]]]
	result = [1,0]
	printing_results(data_set,result,mode)

def check_entropy():
	data_set = [[[0],[1],[1],[1],[0],[1],[1],[1]],[[0],[0],[1],[1],[0],[1],[1],[0]],[[0],[0],[0],[0],[0],[0],[0],[0]]]
	result = [0.811,1.0,0]
	printing_results(data_set,result,entropy)

def check_gain_ratio_nom():
	attr = 1
	data_set = [[[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]]
	,[[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]]
	,[[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]]]
	result = [0.11470666361703151, 0.2056423328155741, 0.06409559743967516]
	total = 0
	for i in xrange(len(data_set)):
		GRNom = gain_ratio_nominal(data_set[i],attr)
		if GRNom is not None and abs(GRNom - result[i]) < EPSILON:
			print "Passed %d"%(i+1)
			total += 1
		else:
			print "Failed %d"%(i+1)
	print "Not all tests were met please look at gain_ratio_nominal" if total != len(result) else "All tests passed"

def check_gain_ratio_num():
	step = [2,4,1]
	data_set = [[[0,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]]
	,[[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]]
	,[[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]]]
	result = [(0.31918053332474033, 0.64),(0.11689800358692547, 0.94),(0.23645279766002802, 0.29)]
	total = 0
	for i in xrange(3):
		GRNum = gain_ratio_numeric(data_set[i],1,step[i])
		if GRNum is not None and reduce(lambda x,y: x and y, (abs(x - y) < EPSILON for x,y in zip(GRNum, result[i]))):
			print "Passed %d"%(i+1)
			total += 1
		else:
		 	print "Failed %d"%(i+1) + str(GRNum)
	print "Not all tests were met please look at gain_ratio_num" if total != len(result) else "All tests passed"

def check_split_on_nominal():
	attr = 1
	data_set = [[[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]],
	[[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]]]
	result = [{0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}
	,{0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}]
	total = 0
	for i in xrange(len(data_set)):
		if split_on_nominal(data_set[i],1) == result[i]:
			print "Passed %d"%(i+1)
			total += 1
		else:
			print "Failed %d"%(i+1)
	print "Not all tests were met please look at split_on_nominal" if total != len(result) else "All tests passed"

def printing_results(data_set,result,function):
	total = 0
	for i in xrange(len(data_set)):
		printfunc = function(data_set[i])
		if printfunc is not None and abs(printfunc - result[i]) < EPSILON:
			print "Passed %d"%(i+1)
			total += 1
		else:
			print "Failed %d"%(i+1)
	print "Not all tests were met please look at %s"% function.__name__ if total != len(result) else "All tests passed"

def check_classify():
	n0 = Node()
	n0.label = 1
	i = 0;
	if n0.classify([0, 1, 2]) == 1:
		print "Passed 1"
		i += 1
	else:
		print "Failed 1"
	n1 = Node()
	n1.label = 0
	n = Node()
	n.label = None
	n.decision_attribute = 1
	n.is_nominal = True
	n.name = "You saw the attributes what do you think?"
	n.children = {1: n0, 2: n1}
	if n.classify([0, 2]) == 0:
		print "Passed 2"
		i += 1
	else:
		print "Failed 2"
	if i == 2:
		print "All tests passed"
	else:
		print "Not all tests passed, look at classify"

def check_ID3():
   attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
   data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
   numerical_splits_count = [5, 5]
   n = ID3(data_set, attribute_metadata, numerical_splits_count, 0)
   fails = 0;
   if n and n.label == 1:
      print "Passed 1"
   else:
      print "Failed 1"
      fails += 1
   attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
   data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
   numerical_splits_count = [1, 1]
   n = ID3(data_set, attribute_metadata, numerical_splits_count, 5)
   if n and [n.classify(x) == x[0] for x in data_set] == [True, False, True, True, False, True, True, True, True, True, True]:
      print "Passed 2"
   else:
      print "Failed 2"
      fails += 1

   attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
   data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
   numerical_splits_count = [5, 5]
   n = ID3(data_set, attribute_metadata, numerical_splits_count, 5)
   print [n.classify(x) == x[0] for x in data_set]
   if n and [n.classify(x) == x[0] for x in data_set] == [True, False, True, True, True, True, True, True, True, True, True]:
      print "Passed 3"
   else:
      print "Failed 3"
      fails += 1
   if fails > 0:
      print "not all tests passed, please see ID3."
   else:
      print "all tests passed."
test = grader( **options )