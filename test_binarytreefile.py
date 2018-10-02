import unittest
from binarytreefile import *

class TestRoot(unittest.TestCase):

    def test_root(self):
        #Create a root, test that the node now have a value
        Bintree = BinaryTree()
        Bintree.add("10")
        root = Bintree.root
        self.assertIsNotNone(root)


if __name__ == '__main__':
    unittest.main()
