import sys

class Node():

    def __init__(self, value = None, arrow = None ):
        self.value = value #The node's value
        self.arrow = [arrow] #This will be a list of the objects that the node are pointing at


class DAGclass():

    def __init__(self):
        """graph with a list of all the nodes and arrows/vertices and edges"""
        self.graph = None
        

    def add(self, node, arrow = None):
        """adds a node to the graph"""
##        print(node)
        self.graph = addNode(self.graph, node, arrow)


    def addArrow(self, newnode, arrow):
        """Add an arow between two already exisiting nodes"""
        contain1 = self.contains(newnode)
        contain2 = self.contains(arrow)
        
        if contain1 and contain2:
            #Both nodes must already be in the graph
            
            for node in self.graph:
                if node.value == newnode:
                    for arrowNode in self.graph:
                        if arrowNode.value == arrow:
                            node.arrow.append(arrowNode)
                            #Something here is wrong I think, the other node that the node is pointing to needs to be append as an object in the list of arrows. 

        elif contain1 is False and contain2:
            return str(value1) + " is not in the graph"

        elif contain2 is False and contain1:
            return str(value2) + " is not in the graph"
        
        else:
            return str(value1) + " and " + str(value2) + " are not in the graph"
        

    
    def contains(self, value):
        """checks if the value is in the graph"""
        if self.graph == None:
            sys.exit("There are no values in the graph")
            #Kan inte använda sys.exit iom unittesting, try or except?????
            
        else:
            return contain(self.graph, value)

        
    def LCA(self, value1, value2):
        """checks that the values for LCA are in the graph"""
        contain1 = self.contains(value1)
        contain2 = self.contains(value2)

##        for node in self.graph:
##            print(node.value)
        
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
        
    
def addNode(graph, newnode, arrow):
    """adds the newnode to the graph, also finds the parent that the arrow is pointing to"""
    if graph == None:
        #If graph is None the graph is empty,
        #The node can not have an arrow pointing at something
        if arrow == None:
            node  = Node(newnode)
            graph = []
            graph.append(node)
        else:
            sys.exit("The graph is empty, the node can't have a parent")
            
    else:
        for node in graph:
            if node.value == arrow:
                parent = node
                break
            
        node = Node(newnode,parent)
        graph.append(node)

    return graph


def contain(graph, value):
    """Goes through the nodes to see that the value is in the graph"""
    for node in graph:
        if node.value == value:
            return True

    return False


def lowest(graph, value1, value2):
    """Finds the path for both values, then checks the LCA"""
    path1 = []
    onePath = []
    onePath.append(value1)
    path1 = pathDAG(graph, value1, path1, onePath)

    path2 = []
    onePath = []
    onePath.append(value2)
    path2 = pathDAG(graph, value2, path2, onePath)

    count = 0
    dictLCA = {} #If there are several paths, the diferent LCAs is saved here

    for path in path1:
        for node1 in path:
            for paths in path2:
                for node2 in paths:
                    count +=1
                    if node1 == node2:
                        dictLCA[count] = node1
                        count = 0
                        break
                else:
                    continue #executed if inner loop do not breaks
                break #executed if inner loop do break
            else:
                continue
            break #Will break when finding the LCA for each path

                
    return dictLCA[min(dictLCA)] #min() looks for the CA with the shortest path
         

def pathDAG(graph, value, path, onePath):
    """Find the path via recursive function.
    Starts with adding the value, then all the nodes to the root in the list path"""
    for node in graph:
        if node.value == value:
            for vertex in node.arrow:
                if vertex == None:
                    path.append(onePath)
                    break
                    
                else:
                    onePath.append(vertex.value)
                    pathDAG(graph, vertex.value, path, onePath)
                    onePath = [onePath[0]]
                    
    return path
    
    
