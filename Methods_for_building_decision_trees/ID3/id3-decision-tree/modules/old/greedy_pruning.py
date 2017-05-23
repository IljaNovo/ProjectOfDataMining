def reduced_error_pruning(root, training_set, validation_set):
    """Greedy reduced error pruning for a trained ID3 decision tree.
    
    Greedily removes nodes to improve validation accuracy.
    
    Arguments:
        root {Node} -- root node of decision tree learned over the training set
        training_set {List of Examples} -- list of examples given as lists of attribute values
        validation_set {List of Examples} -- list of examples disjoint from the training set, given as lists of attribute values

    Returns:
        Node -- the improved root of the pruned decision tree
    """

    # Compute the original accuracy for comparison
    accuracy = validation_accuracy(root, validation_set)
    print "Original accuracy: " + str(accuracy)

    # Initialize gain to accuracy to simulate do-while
    gain = accuracy

    while gain > 0:
        # Build list of nodes by traversing breadth first
        nodes = [root]
        for n in nodes:
            if n.children:
                if n.is_nominal:
                    nodes.extend(x for x in n.children.values())
                else:
                    nodes.extend(x for x in n.children)

        # if len(set(nodes)) != len(nodes):
        #     raise Exception("you literally fucked up BFS")

        performance = []

        for n in nodes:
            if n.label is not None:
                # If leaf, skip node
                performance.append(None)
            else:
                # Temporarily make it a leaf to compute validation accuracy
                n.make_leaf()
                acc = validation_accuracy(root, validation_set)
                performance.append(acc)
                n.make_fork()

        i, max_performance = max(enumerate(performance), key=lambda x: x[1])
        if max_performance >= accuracy:
            gain = max_performance - accuracy
            accuracy = max_performance
            print "Increased accuracy by %f" % (gain)

            # Permanently make the node a leaf
            nodes[i].make_leaf()

    return root
