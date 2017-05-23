from node import Node
from ID3 import *
from operator import xor

# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root, training_set, validation_set):
    """NONGREEDY reduced error pruning
    """

    # Compute the original accuracy for comparison
    accuracy = validation_accuracy(root, validation_set)
    print "Original accuracy: " + str(accuracy)

    # Initialize gain to accuracy to simulate do-while
    gain = accuracy

    nodes = [root]

    while len(nodes) > 0:
        n = nodes.pop()
        
        # Check if n is a fork
        if n.label is None:
            # Temporarily make it a leaf to compute validation accuracy
            n.make_leaf()
            acc = validation_accuracy(root, validation_set)
            n.make_fork()

            if acc >= accuracy:
                gain = acc - accuracy
                accuracy = acc
                print "Increased accuracy by %f" % (gain)

                # Permanently make the node a leaf
                n.make_leaf()
            else:
                try:
                    if n.is_nominal:
                        nodes.extend(x for x in n.children.values())
                    else:
                        nodes.extend(x for x in n.children)
                except (KeyError, IndexError):
                    print "No children found something's probably wrong"

    return root


def validation_accuracy(tree,validation_set):
    """Takes a tree and a validation set, and returns the accuracy of the set on the given tree in terms of correctly classified instances.
    
    Arguments:
        tree {Node} -- the root of the decision tree learned over a set of training data
        validation_set {List of Examples} -- list of examples given as sequences of attribute values
    
    Returns:
        {Float} -- percentage of correctly classified instances
    """

    total_instances = len(validation_set)
    accurate_instances = 0

    for x in validation_set:
        true_class = x[0]  # winner classification
        computed_class = tree.classify(x)
        if computed_class == true_class:
            accurate_instances += 1

    accuracy = accurate_instances / float(total_instances)
    return accuracy

