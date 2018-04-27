from ID3 import *
from node import *

def dnf(tree):

    AND = " ^ "
    OR = " v "

    child_output = []

    if tree.is_nominal:
        for value, child in tree.children.items():
            output = ""

            # If child is a positive leaf, return the cumulative value
            if child.label == 1:
                output = "%s = %s" % (tree.name, value)

            # If child is a subtree, recursively concatenate using AND
            if child.children and dnf(child):
                output += AND + dnf(child)
            
            child_output.append(output)

    else:
        # Tree splits on numeric attribute
        if tree.children:
            for i, child in enumerate(tree.children):
                output = ""
                comparison = "<" if i == 0 else ">="

                if child.label == 1:
                    output = "%s %s %f" % (tree.name, comparison, tree.splitting_value)

                if child.children and dnf(child):
                    output += AND + "%s %s %f" % (tree.name, comparison, tree.splitting_value) + dnf(child)

                child_output.append("(%s)" % (str(output)))

    if len(child_output) == 0:
        result = ""
    elif len(child_output) == 1:
        result = child_output[0]
    else:
        result = OR.join(child_output)
        print (child_output)

    return result








    # # Otherwise, print attribute split information
    # else:
    #     if tree.is_nominal:
    #         for val, child in tree.children.items():
    #             output += "(%s = %s)" % (tree.name, val)
    #             output += dnf(child)
    #     else:
    #         # Node is numerical
    #         output += "%s%s < %f" % (pre, self.name, self.splitting_value) + "\n"
    #         output += dnf(tree.children[0])
    #         output += "%s%s >= %f" % (pre, self.name, self.splitting_value) + "\n"
    #         output += dnf(tree.children[1])


if __name__ == "__main__":
  # Tests for ID3
  attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
  data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
  numerical_splits_count = [5, 5]

  test = ID3(data_set, attribute_metadata, numerical_splits_count, 10)

  test0 = ID3(data_set, attribute_metadata, numerical_splits_count, 0)
  print ("test:")
  print (test.print_tree())

  print ("test0:")
  print (test0.print_tree())
  print (dnf(test))
  print (dnf(test0))
  # dnf()