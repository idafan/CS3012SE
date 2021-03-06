import unittest
from binarytreefile import *

class TestRoot(unittest.TestCase):

    def test_root(self):
        #Create a root, test that the node now have a value
        Bintree = BinaryTree()
        Bintree.add(10)
        
        self.assertIsNotNone(Bintree.root)

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


    def test_contain(self):
        Bintree = BinaryTree()
        numbers = [10, 8, 15, 2, 12, 9, 18]
        for number in numbers:
            Bintree.add(number)
            
        self.assertTrue(Bintree.contains(10))
        self.assertTrue(Bintree.contains(2))
        self.assertTrue(Bintree.contains(18))
        self.assertFalse(Bintree.contains(4))

    def test_LCA(self):
        Bintree = BinaryTree()
        numbers = [10, 8, 15, 2, 12, 9, 18]
        for number in numbers:
            Bintree.add(number)
        self.assertEqual(Bintree.LCA(15,8),10)
        self.assertEqual(Bintree.LCA(2,9),8)
        self.assertSequenceEqual(Bintree.LCA(4,8), "4 is not in the binary tree")
        self.assertSequenceEqual(Bintree.LCA(2,3), "3 is not in the binary tree")
        self.assertSequenceEqual(Bintree.LCA(24,6), "24 and 6 are not in the binary tree")
        


if __name__ == '__main__':
    unittest.main()
