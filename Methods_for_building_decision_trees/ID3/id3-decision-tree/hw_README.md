### Decision Tree Starter Code
#Credits: Philip Lan, Christopher Li, Alex Wang, Jacob Samson, Nishant Subramani

### Building

To build the project, you must pass it a dictionary of inputs.Below are listed the options available to be passed.

## Documentation
train
	Required. Should be passed a path from the decision_tree_driver.py file to the file to be trained on.
validate
	Should be passed a path from the decision_tree_driver.py file to the file to be validated on or left blank.
predict
	Should be passed a path from the decision_tree_driver.py file to the file to predict outputs. The generated output will be created and named after this file in the format of file_predictions.csv or left blank.
limit_splits_on_numerical
	Should be passed an integer that limits the number of splits that can be made on each numerical attribute.
limit_depth
	Should be passed an integer that limits depth of the decision tree.
print_tree
	Should be passed a boolean which will print a tree in readable format if True.
print_dnf
	Should be passed a boolean which will print a disjunctive normalized form of the decision tree if True.
prune
	Should be passed a boolean which prune the tree with the reduced error pruning method if True. Requires validate.
learning_curve
	Should be passed a dictionary of upper bound and increment or left blank. This will take a portion of the training data and validates it on the validation set and will be done over a range of partials. The plot will be saved in the output directory.


### Example

Below are the commands necessary to run the program. The options dictionary is customizable based on the documentation above. 

	execfile("decision_tree_driver.py")
	options = {
	    'train' : 'data/btrain.csv',
	    'validate': 'data/bvalidate.csv',
	    'predict': 'data/btest.csv',
	    'limit_splits_on_numerical': 5,
	    'limit_depth': 20,
	    'print_tree': True,
	    'print_dnf' : True,
	    'prune' : True,
	    'learning_curve' : {
	    	'upper_bound' : 0.01,
	    	'increment' : 0.001
		}
	}
	decision_tree_driver(options)

The only variable required is train, so the program will not output anything, it can also execute with only the train key:

	execfile("decision_tree_driver.py")
	options = {
		'train': 'data/btrain.csv'
	}
	decision_tree_driver(options)

