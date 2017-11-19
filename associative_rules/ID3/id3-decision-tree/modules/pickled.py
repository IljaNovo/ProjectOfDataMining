#NOTE: you don't need to change anything in this function
import pickle

def makePickle(obj, filename):
  f = open(filename, "wb")
  p = pickle.Pickler(f)
  p.dump(obj)
  f.close()

def loadPickle(filename):
	f = open(filename, "rb")
	u = pickle.Unpickler(f)
	ret = u.load()
	f.close()
	return ret