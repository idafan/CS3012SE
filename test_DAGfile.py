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





if __name__ == '__main__':
    unittest.main() 
