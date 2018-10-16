import unittest
from DAGfile import *

class TestDAG(unittest.TestCase):

    def test_oneNode(self):
        Graph = DAGclass()
        Graph.add("A")
        LCA = Graph.LCA("A", "A")
        self.assertEqual(LCA, "A")
        
"""
There are no values in the graph
You can only have one root, you must assign a parent to the node
There are no values in the graph
There are no values in the graph
Can't find the LCA
F
======================================================================
FAIL: test_oneNode (__main__.TestDAG)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\idafn\Documents\GitHub\CS3012SE\test_DAGfile.py", line 10, in test_oneNode
    self.assertEqual(LCA, "A")
AssertionError: None != 'A'

----------------------------------------------------------------------
Ran 1 test in 0.045s

FAILED (failures=1)
"""








if __name__ == '__main__':
    unittest.main() 
