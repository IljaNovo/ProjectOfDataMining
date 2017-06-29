import random
from ID3 import *
from operator import xor
from parse import parse
import matplotlib.pyplot as plt
import os.path
from pruning import validation_accuracy
from modules.pruning import *

# NOTE: these functions are just for your reference, you will NOT be graded on their output
# so you can feel free to implement them as you choose, or not implement them at all if you want
# to use an entirely different method for graphing

def get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, pct):
    '''
    get_graph_accuracy_partial - Given a training set, attribute metadata, validation set, numerical splits count, and percentage,
    this function will return the validation accuracy of a specified (percentage) portion of the trainging setself.
    '''
    length = len(train_set) * pct
    new_data_set = random.sample(train_set, int(length))
    tree = ID3(new_data_set, attribute_metadata, numerical_splits_count, 20)
    # reduced_error_pruning(tree, new_data_set, validate_set)
    accuracy = validation_accuracy(tree, validate_set)
    return accuracy


def get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, iterations, pcts):
    '''
    Given a training set, attribute metadata, validation set, numerical splits count, iterations, and percentages,
    this function will return an array of the averaged graph accuracy partials based off the number of iterations.
    '''
    total = 0
    arr = []
    accuracies = {}
    for pct in pcts:
        for i in range(0, iterations):
            accuracy = get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, pct)
            if pct not in accuracies:
                accuracies[pct] = [accuracy]
            else:
                accuracies[pct].append(accuracy)
    print (accuracies)

    # for i in range(1, 11):    
    #     for j in range(0, iterations):
    #         total += get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, 0.1 * i)
    #         j += 1
    #     avg = float(total)/float(iterations)
    #     arr.append(avg)
    #     i += 1
    # return arr
# get_graph will plot the points of the results from get_graph_data and return a graph
def get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment):
    '''
    get_graph - Given a training set, attribute metadata, validation set, numerical splits count, depth, iterations, lower(range),
    upper(range), and increment, this function will graph the results from get_graph_data in reference to the drange
    percentages of the data.
    '''
    pass












