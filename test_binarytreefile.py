import unittest
from binarytreefile import *

class TestRoot(unittest.TestCase):

    def test_root(self):
        #Create a root, test that the node now have a value
        Bintree = BinaryTree()
        Bintree.add(10)
        root = Bintree.root
        self.assertIsNotNone(root)

    def test_nodes(self):
        Bintree = BinaryTree()
        Bintree.add(10)
        Bintree.add(8)
        Bintree.add(15)
        Bintree.add(2)
        Bintree.add(12)
        self.assertEqual(Bintree.root.value, 10)
        self.assertEqual(Bintree.root.less.value, 8)
        self.assertEqual(Bintree.root.greater.value, 15)
        self.assertEqual(Bintree.root.less.less.value, 2)
        self.assertEqual(Bintree.root.greater.less.value, 12)
        


if __name__ == '__main__':
    unittest.main()
