import unittest
from binarytreefile import *

class TestRoot(unittest.TestCase):

    def test_root(self):
        #Create a root, test that the node now have a value
        Bintree = BinaryTree()
        Bintree.add("10")
        root = Bintree.root
        self.assertIsNotNone(root)

    def test_nodes(self):
        Bintree = BinaryTree()
        Bintree.add("10")
        Bintree.add("8")
        Bintree.add("15")
        self.assertEqual(Bintree.root.value, "10")
        self.assertEqual(Bintree.root.less.value, "8")
        self.assertEqual(Bintree.root.greater.value, "15")


if __name__ == '__main__':
    unittest.main()



##F
##======================================================================
##FAIL: test_root (__main__.TestRoot)
##----------------------------------------------------------------------
##Traceback (most recent call last):
##  File "C:\Users\idafn\Documents\GitHub\CS3012SE\test_binarytreefile.py", line 11, in test_root
##    self.assertIsNotNone(root)
##AssertionError: unexpectedly None
##
##----------------------------------------------------------------------
##Ran 1 test in 0.008s
##
##FAILED (failures=1)
##
    
"""added return node in addNode()"""

##
##.
##----------------------------------------------------------------------
##Ran 1 test in 0.011s
##
##OK

##E.
##======================================================================
##ERROR: test_nodes (__main__.TestRoot)
##----------------------------------------------------------------------
##Traceback (most recent call last):
##  File "C:\Users\idafn\Documents\GitHub\CS3012SE\test_binarytreefile.py", line 16, in test_nodes
##    Bintree.add("8")
##  File "C:\Users\idafn\Documents\GitHub\CS3012SE\binarytreefile.py", line 18, in add
##    self.root = addNode(self.root, node)
##  File "C:\Users\idafn\Documents\GitHub\CS3012SE\binarytreefile.py", line 29, in addNode
##    elif newnode > node:
##TypeError: '>' not supported between instances of 'str' and 'Node'
##
##----------------------------------------------------------------------
##Ran 2 tests in 0.019s
##
##FAILED (errors=1)
##
##

"""changed ">" to "<" in the if-statement, 8 is added to the tree"""

##E.
##======================================================================
##ERROR: test_nodes (__main__.TestRoot)
##----------------------------------------------------------------------
##Traceback (most recent call last):
##  File "C:\Users\idafn\Documents\GitHub\CS3012SE\test_binarytreefile.py", line 20, in test_nodes
##    self.assertEqual(Bintree.root.greater.value, "15")
##AttributeError: 'NoneType' object has no attribute 'value'
##
##----------------------------------------------------------------------
##Ran 2 tests in 0.010s
##
##FAILED (errors=1)

"""it doesn't work to add 15 to the tree, the data in Bintree.root.greater is None"""
