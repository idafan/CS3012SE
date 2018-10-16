class Node():

    def __init__(self, value = None, arrow = None ):
        self.parent = None
        self.value = value #The node's value
        self.arrow = arrow #This will be a list of the objects that the node are pointing at


class DAGclass():

    def __init__(self):
        self.root = None

    def add(self, node, parent = None):
        """adds a node to the binary tree"""
        self.contains(parent)
        self.root = addNode(self.root, node, parent)
    
    def contains(self, value):
        if self.root == None:
            print("There are no values in the graph")
            return False
        else:
            nodeObject = contain(self.root, value)
            
            if nodeObject == False:
                print("Cant find " + str(value) + "in the graph")

            else:
                return nodeObject
        
    def LCA(self, value1, value2):
        """checks that the values for LCA are in the graph"""
        contain1 = self.contains(value1)
        contain2 = self.contains(value2)
        if contain1 == False or contain2 == False:
            print("Can't find the LCA")
            
        else:
            return lowest(self.root, contain1, contain2)

        
        
    
def addNode(root, newnode, parent):

    if parent == None:
        try:
            if node == None: #Limits the graph to have only one root
                node  = Node(newnode)
        except:
            print("You can only have one root, you must assign a parent to the node")
            
    node = None

    return node


def contain(node, value):

    if node.value == value:
        return node

    if node.arrow == None:
        return False
    
    else:
        for vertex in node.arrow:
            return contain(vertex, value)

def lowest(node, value1, value2):
    """Finding the path from value1 to the root"""
    path1 = []
    if value1.parent == None:
        path1.append(value1.value)

    """Finding the path for value2 but compare this to the path of value1"""
    if value2.parent == None:
        for node in path1:
            if node.value == value2:
                return value2
         
         


##def path():
##    """Find the path via recursive function??"""
##    
    
    

    
        
    
        


    
        

    
