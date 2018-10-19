import unittest
from DAGfile import *

class TestDAG(unittest.TestCase):

##    def test_oneNode(self):
##        #A graph with one node
##        #The LCA of one node is the node itself
##        Graph = DAGclass()
##        Graph.add("A")
##        LCA = Graph.LCA("A", "A") 
##        self.assertEqual(LCA, "A")
##
##
##    def test_oneLine(self):
##        #A line of nodes
##        #The LCA in a line will be the node that is the furthest up in the graph
##        Graph = DAGclass()
##        Graph.add("A")
##        Graph.add("B","A")
##        Graph.add("C","B")
##        Graph.add("D","C")
##        Graph.add("E","D")
##        Graph.add("F","E")
##        self.assertEqual(Graph.LCA("A","C"), "A")
##        self.assertEqual(Graph.LCA("C","B"), "B")
##        self.assertEqual(Graph.LCA("D","F"), "D")
##
##
##    def test_binaryTree(self):
##        Graph = DAGclass()
##        Graph.add("A")
##        Graph.add("B","A")
##        Graph.add("C","A")
##        Graph.add("D","B")
##        Graph.add("E","B")
##        Graph.add("F","C")
##        Graph.add("G","C")
##        self.assertEqual(Graph.LCA("D","C"), "A")
##        self.assertEqual(Graph.LCA("G","F"), "C")
##        self.assertEqual(Graph.LCA("B","E"), "B")

    def test_DAG(self):
        Graph = DAGclass()
        Graph.add("A")
        Graph.add("B","A")
        Graph.add("C","B")
        Graph.add("D","A")
        Graph.add("E","D")
        Graph.add("F","C")
        Graph.addArrow("F","E")
##        self.assertEqual(Graph.LCA("E","C"), "A")
##        self.assertEqual(Graph.LCA("C","B"), "B")
##        self.assertEqual(Graph.LCA("F","C"), "C")
        self.assertEqual(Graph.LCA("F","E"), "E")
        

        

##    def test_noNode(self):
##        Graph = DAGclass()
##        self.assertRaises()


if __name__ == '__main__':
    unittest.main() 





