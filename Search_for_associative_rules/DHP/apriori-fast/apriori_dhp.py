import sys
import os
from collections import defaultdict
import time
start_time = time.time()

# data; frozenset
# return: list of 2-item frozensets 
def generate_2items_sets(data):
	data = sorted(data)
	lst = []
	i = 1
	for a in data:
		for b in data[i:]:
			lst.append(frozenset([a,b]))
		i += 1
	return lst

# @param: dataset<list<frozenset>>
# @param: support<int>
# @return: results<dict<frozenset: int>>; dhp<Counter>
def get_frequent_single_items(dataset,support,results):
	single_counter = defaultdict(int)
	dhp = defaultdict(int)
	for data in dataset:
		for item in generate_2items_sets(data):
			dhp[item] += 1
		for each in data:
			single_counter[each] += 1
	for k in single_counter:
		if single_counter[k] >= support: 
			results[frozenset([k])] = single_counter[k]
	return dhp

# candidates: <dict<frozenset: int>>
# c: frozenset
def isFrequent(candidates, c):
	for each in c:
		one_subset = c-frozenset([each])
		if one_subset not in candidates:
			# print one_subset
			return False
	return True

# @param: candidates<dict<frozenset: int>>
# @param: k<int>
# return: results<set<frozenset>>
def generate_candidates(candidates,k):
	res = set()
	for a in candidates:
		for b in candidates:
			c = a | b
			if len(c)==k and a != b:
				if isFrequent(candidates, c):
					res.add(c)
	return res

# @param: dataset<list<frozenset>>
# @param: candidates<dict<frozenset: int>>
# @return counted<Counter<frozenset: int>>
def count_candidates(dataset, candidates):
	counted = defaultdict(int)
	for instance in dataset:
		bucket = [candidate for candidate in candidates if candidate <= instance]
		for each in bucket:
			counted[each] += 1
	return counted


# @param: counted<dict<frozenset: int>>
# @param: support<int>
# @return: results<dict<frozenset: int>>
def generate_support_candidates(counted, support):
	results = {}
	for item in counted:
		if counted[item] >= support:
			# key = frozenset(sorted(item))
			# print key
			results.update({item:counted[item]})
	return results

# @param: dataset<list<frozenset>>
# @param: support<int>
# @return: results<dict<frozenset: int>>
def apriori(dataset, support):
	results = {}
	candidates = get_frequent_single_items(dataset, support, results)
	print 'This is the 2 iteration'
	support_candidates = {}
	if candidates:
		for item in candidates:
			if candidates[item] >= support:
				support_candidates.update({item: candidates[item]})
	results.update(support_candidates)
	candidates = support_candidates
	k = 3
	while candidates:
		print 'This is the %d iteration' % k
		candidates = generate_candidates(candidates.keys(), k)
		if not candidates: break
		counted = count_candidates(dataset, candidates)
		support_candidates = generate_support_candidates(counted, support)
		results.update(support_candidates)
		candidates = support_candidates
		k += 1
	return results



dataset = sys.argv[1]
lines = []
with open(dataset, 'r') as f:
	for line in f.readlines():
		line = frozenset([int(each) for each in line.split()])
		lines.append(line)
dataset = lines
support = int(sys.argv[2])
outputfile = sys.argv[3]
results = apriori(dataset, support)
print "This whole program takes about %f" % (time.time()-start_time)
print len(results)
# for item,count in results.iteritems():
# 	itemstring = ' '.join(str(e) for e in item)
# 	string = '%s (%d)' % (itemstring,count)
# 	print string

with open('output.txt','w') as out:
	for item,count in results.iteritems():
		item = sorted(item)
		itemstring = ' '.join(str(e) for e in item)
		string = '%s (%d)\n' % (itemstring,count)
		out.write(string)

res = []
with open('output.txt') as f:
	for line in f.readlines():
		line = line.split()
		res.append((line[:-1],line[-1]))


# a: tuple<list of strs, str>
# b : tuple<list of srts, str>
def hang_cmp(a, b):
	i = 0
	len_a = len(a[0])
	len_b = len(b[0])
	while i < len_a and i < len_b:
		if int(a[0][i]) > int(b[0][i]):
			return 1
		elif int(a[0][i]) < int(b[0][i]):
			return -1
		else:
			i += 1
			continue
	if i >= len_a and i >= len_b:
		return 0
	elif i < len_a:
		return 1
	else:
		return -1

res = sorted(res, cmp=hang_cmp)
with open('output.txt','w') as out:
	for each in res:
		itemstring = ' '.join(each[0])
		String = itemstring + ' ' + each[1] + '\n'
		out.write(String)




