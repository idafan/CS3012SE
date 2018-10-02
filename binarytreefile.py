#classes to create a binary tree

class Node():

    def __init__(self,value):
        self.value = value
        self.less = None
        self.greater = None


class Bintree():

    def __init__(self):
        self.root = None

    def add(self, node):
        #adds a node to the binary 
        addNode(self.root, node)


def addNode(node, newnode):
    #The function who finds where to add the new node
    #Checks three different cases

    #If node==Node is true a new node will be added
    if node == None:
        node  = Node(newnode)

    elif newnode > node:
        #If the newnode is greater than the node there is two cases

    else:
        #Two cases where the newnode is less then the node
        


    
        

    
