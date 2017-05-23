# from ..modules.ID3 import *

def id3_tests():
    # Tests for check_homogenous
    data_set = [[0],[1],[1],[1],[1],[1]]
    assert(check_homogenous(data_set) == None)
    data_set = [[0],[1],[None],[0]]
    assert(check_homogenous(data_set) == None)
    data_set = [[1],[1],[1],[1],[1],[1]]
    assert(check_homogenous(data_set) == 1)
    print "Passed tests for check_homogenous"

    # Tests for mode
    data_set = [[0],[1],[1],[1],[1],[1]]
    assert(mode(data_set) == 1)
    data_set = [[0],[1],[0],[0]]
    assert(mode(data_set) == 0)
    print "Passed tests for mode"

    # Tests for split_on_nominal
    data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
    assert(split_on_nominal(data_set, attr) == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]})
    data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
    assert(split_on_nominal(data_set, attr) == {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]})
    print "Passed tests for split_on_nominal"

    # Tests for split_on_numerical
    d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48
    assert(split_on_numerical(d_set,a,sval) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]]))
    d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
    assert(split_on_numerical(d_set,a,sval) == ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]]))
    print "Passed tests for split_on_numerical"

    # Tests for entropy
    data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
    assert round(entropy(data_set), 3) == 0.811
    data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
    assert entropy(data_set) == 1.0
    data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
    assert entropy(data_set) == 0
    print "Passed tests for entropy"

    # Tests for gain_ratio_nominal
    data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
    assert gain_ratio_nominal(data_set,attr) == 0.11470666361703151
    data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
    assert gain_ratio_nominal(data_set,attr) == 0.2056423328155741
    data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
    assert gain_ratio_nominal(data_set,attr) == 0.06409559743967516
    print "Passed tests for gain_ratio_nominal"

    # Tests for gain_ratio_numeric
    data_set,attr,step = [[0,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
    assert gain_ratio_numeric(data_set,attr,step) == (0.31918053332474033, 0.64)
    data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
    assert gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
    data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
    assert gain_ratio_numeric(data_set,attr,step) == (0.23645279766002802, 0.29)
    print "Passed tests for gain_ratio_numeric"

    # Tests for pick_best_attribute
    numerical_splits_count = [20,20]
    attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
    data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
    assert pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)
    attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
    data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
    assert pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)
    print "Passed tests for pick_best_attribute"

    # Tests for ID3
    attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
    data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
    numerical_splits_count = [5, 5]

    test = ID3(data_set, attribute_metadata, numerical_splits_count, 0)
    print "\n"
    test.print_tree()
    # print "Passed tests for ID3"

    print "All tests passed"