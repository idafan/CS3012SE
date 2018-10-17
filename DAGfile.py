import sys

class Node():

    def __init__(self, value = None, arrow = None ):
        self.value = value #The node's value
        self.arrow = arrow #This will be a list of the objects that the node are pointing at


class DAGclass():

    def __init__(self):
        self.graph = None
        

    def add(self, node, parent = None):
        """adds a node to the binary tree"""

        self.graph = addNode(self.graph, node, parent)

    
    def contains(self, value):
        if self.graph == None:
            sys.exit("There are no values in the graph")
            
        else:
            nodeObject = contain(self.graph, value)
            
            if nodeObject == False:
                sys.exit("Cant find " + str(value) + "in the graph")

            else:
                return nodeObject


        
    def LCA(self, value1, value2):
        """checks that the values for LCA are in the graph"""
        contain1 = self.contains(value1)
        contain2 = self.contains(value2)
        
        if contain1 and contain2:
            #if both values are in the graph the LCA is checked
            return lowest(self.graph, value1, value2)

        elif contain1 is False and contain2:
            return str(value1) + " is not in the graph"

        elif contain2 is False and contain1:
            return str(value2) + " is not in the graph"
        else:
            return str(value1) + " and " + str(value2) + " are not in the graph"

        

""" -------------------------------- end of classes ---------------------------- """       
        
    
def addNode(graph, newnode, parent):
    
    if graph == None:
        if parent == None: #If graph is None the graph is empty, the node can not have a parent
            node  = Node(newnode)
            graph = []
            graph.append(node)
        else:
            sys.exit("The graph is empty, the node can't have a parent")
            
    else:
        node = Node(newnode,parent)
        graph.append(node)

    return graph


def contain(graph, value):

    for vertex in graph:
        if vertex.value == value:
            return True

    return False


def lowest(graph, value1, value2):
    """Finding the path from value1 to the root"""
    path1 = []
    path1.append(value1)
    path1 = pathDAG(graph, value1, path1) 

    path2 = []
    path2.append(value2)
    path2 = pathDAG(graph, value2, path2)

    for node1 in path1:
        for node2 in path2:
            if node1 == node2:
                return node1       
         

def pathDAG(graph, value, path):
    """Find the path via recursive function
    starts with adding the value, then all the nodes to the root"""
    
    for vertex in graph:
        if vertex.arrow != None:
            for node in vertex.arrow:
                if node == value:
                    path.append(node.value)
                    pathDAG(graph, node.value, path)

    return path
    
        
            
        
    
    
    
    

    
        
    
        


    
        

    
