import unittest
from DAGfile import *

class TestDAG(unittest.TestCase):

    def test_oneNode(self):
        #A graph with one node
        #The LCA of one node is the node itself
        Graph = DAGclass()
        Graph.add("A")
        LCA = Graph.LCA("A", "A") 
        self.assertEqual(LCA, "A")


    def test_oneLine(self):
        #A line of nodes
        #The LCA in a line will be the node that is the furthest up in the graph
        Graph = DAGclass()
        Graph.add("A")
        Graph.add("B","A")
        Graph.add("C","B")
        Graph.add("D","C")
        Graph.add("E","D")
        Graph.add("F","E")
        self.assertEqual(Graph.LCA("A","C"), "A")
        self.assertEqual(Graph.LCA("C","B"), "B")
        self.assertEqual(Graph.LCA("D","F"), "D")
        


if __name__ == '__main__':
    unittest.main() 
