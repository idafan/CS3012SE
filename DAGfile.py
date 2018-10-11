class Node():

    def __init__(self, value):
        self.value = value
        self.less = None
        self.greater = None


class BinaryTree():

    def __init__(self):
        self.root = None

    def add(self, node):
        """adds a node to the binary tree"""
        self.root = addNode(self.root, node)

    def contains(self, value):
        """checks if the value is in the binary tree"""
        return contain(self.root, value)

    def LCA(self, value1, value2):
        """checks that the values for LCA are in the graph"""
        contain1 = self.contains(value1)
        contain2 = self.contains(value2)
        if contain1 and contain2:
            #if both values are in the tree the LCA is checked
            return lowest(self.root, value1, value2)

        elif contain1 is False and contain2:
            return str(value1) + " is not in the binary tree"

        elif contain2 is False and contain1:
            return str(value2) + " is not in the binary tree"
        else:
            return str(value1) + " and " + str(value2) + " are not in the binary tree"
        


def addNode(node, newnode):
    """Create a new node-object and add node to the graph"""
    break
        

def contain(node, value):
    """A function to check if the node is in the graph"""
    break


def lowest(node, value1, value2):
    """The LCA-function"""
    break
    
    
        


    
        

    
