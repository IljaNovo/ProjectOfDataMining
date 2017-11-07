from pprint import pprint
from copy import deepcopy

class Node:
    """A class for decision tree nodes.

    Members:
        label {Int}
            - output label (0 or 1) if there are no other attributes to split on at this node, or if the data is homogenous
            - mode output if there is a decision attribute
        decision_attribute {Int}
            - index of the attribute being split on
            - None if leaf node
        is_nominal {Boolean}
            - indicates whether the attribute being split on is nominal (True) or numeric (False)
            - None if leaf node
        value {None} -- unused
        mode {Int} -- mode output classification among examples sorted to this node
        splitting_value {Float}
            - threshold for split if attribute being split on is numeric
            - None if leaf node, or splitting on nominal attribute
        children {List or Dictionary}
            - a list of 2 if numeric, with 0 index holding examples < splitting_value and 1 index holding examples >= splitting_value
            - a dictionary of "value": [subset] pairs if nominal
            - None if leaf node
        name {String}
            - name of the attribute being split on
            - None if leaf node
    """

    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        self.value = None
        self.mode = None
        self.splitting_value = None
        self.children = {}
        self.name = None
        self.saved_children = None

    def make_leaf(self):
        if self.label is None:
            self.label = self.mode
            self.saved_children = self.children
            self.children = {}

    def make_fork(self):
        if self.label is not None:
            self.label = None
            self.children = self.saved_children
            self.saved_children = {}

    def num_nodes(self):
        acc = 1
        if self.children:
            if self.is_nominal:
                children = self.children.values()
            else:
                children = self.children

            for c in children:
                acc += c.num_nodes()

        return acc

    def classify(self, instance):
        """
        given a single observation, will return the output of the tree
        """

        # If node is a leaf, return classification
        if self.label is not None:
            return self.label

        else:
            attr = self.decision_attribute
            instance_val = instance[attr]

            try:
                if self.is_nominal:
                    next = self.children[instance_val]
                else:
                    # Node is numerical
                    if instance_val < self.splitting_value:
                        next = self.children[0]
                    else:
                        # Instance value is >= splitting value
                        next = self.children[1]

                return next.classify(instance)

            # Catch missing attribute values, etc.
            except (IndexError, KeyError):
                return self.mode


    def print_tree(self, indent = 0):
        """
        returns a string of the entire tree in human readable form
        """

        pre = "|    " * indent
        output = ""

        # If node is a leaf, simply print output class
        if self.label is not None:
            output += pre + "CLASS: " + str(self.label) + "\n"

        # Otherwise, print attribute split information
        else:
            if self.is_nominal:
                for val, child in self.children.items():
                    output += "%s%s: %s" % (pre, self.name, val) + "\n"
                    output += child.print_tree(indent + 1)
            else:
                # Node is numerical
                output += "%s%s < %f" % (pre, self.name, self.splitting_value) + "\n"
                output += self.children[0].print_tree(indent + 1)
                output += "%s%s >= %f" % (pre, self.name, self.splitting_value) + "\n"
                output += self.children[1].print_tree(indent + 1)

        return output
        
    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        self.print_dnf_tree_helper()

    def print_dnf_tree_helper(self,lineage=[]):
        new_lineage = deepcopy(lineage)
        if self.label is not None:
            if self.label == 1:
                print ("("),
                for name in new_lineage[:-1]:
                    print (str(name) + " AND"),
                print (new_lineage[-1] + " )")
                print ("OR")
        else:
            if not self.is_nominal:
                new_lineage1 = deepcopy(lineage)
                new_lineage1.append(str(self.name) + " < " + str(self.splitting_value))
                if new_lineage1 is not None:
                    self.children[0].print_dnf_tree_helper(new_lineage1)
                new_lineage2 = deepcopy(lineage)
                new_lineage2.append(str(self.name) + " >= " + str(self.splitting_value))
                if new_lineage2 is not None:
                    self.children[1].print_dnf_tree_helper(new_lineage2)
            else:
                for key, child in self.children.iteritems():
                    new_lineage = deepcopy(lineage)
                    if new_lineage is not None:
                        new_lineage.append(str(self.name) + "=" + str(key))
                    child.print_dnf_tree_helper(new_lineage)
