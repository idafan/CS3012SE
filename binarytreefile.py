#classes to create a binary tree

class Node():

    def __init__(self, value):
        self.value = value
        self.less = None
        self.greater = None


class BinaryTree():

    def __init__(self):
        self.root = None

    def add(self, node):
        #adds a node to the binary tree
        self.root = addNode(self.root, node)

    def contains(self, value):
        #checks if the value is in the binary tree
        return contain(self.root, value)


def addNode(node, newnode):
    #The function who finds where to add the new node, compare the existing value with the newnode
    #Checks three different cases

    #If node==Node is true a new node will be added
    if node == None:
        node  = Node(newnode)

    elif newnode > node.value:
        #If the newnode is greater than the node there is two cases
        #If the node.greater is None, the newnode will be added as a node there
        #If there is a value in node.greater, that value there will be compared with the newnode
        if node.greater == None:
            node.greater = Node(newnode)
        else:
            node.greater = addNode(node.greater, newnode)

    else:
        #The same two cases as above
        if node.less == None:
            node.less = Node(newnode)
        else:
            node.less = addNode(node.less, newnode)


    return node #The node needs to be returned to be saved in self.root
        

def contain(node, value):
    if node == None:
        #If the root is None there are no values in the binary tree
        #If it search through the tree without finding the value, it will eventually reach None
        return False
    
    elif node.value == value:
        #The value has been found
        return True

    elif value >= node.value:
        #It will continue to compare with the greater value
        return contain(node.greater, value)

    elif value <= node.value:
        #Compares with the lesser value
        return contain(node.less, value)

    else:
        #Something is wrong
        return False

    
    
        


    
        

    
