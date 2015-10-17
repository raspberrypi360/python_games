'''
Created on Apr 3, 2015

@author: ryan
'''
import unittest
from tree import *
from bst import *

class Test(unittest.TestCase):


    def setUp(self):
        self.trees = []
        self.trees.append(Tree("#"))
        self.trees.append(Tree("1, #, #"))
        self.trees.append(Tree("1, 2, #, #, #"))
        self.trees.append(Tree("1, #, 2, #, #"))
        self.trees.append(Tree("1, 2, 3, #, #, 4, #, #, #"))
        self.trees.append(Tree("1, 2, 2, 3, 4, 4, 3, #, #, #, #, #, #, #, #"))
        self.trees.append(Tree("5, 3, 7, 2, 4, 6, 8, 1, #, #, #, #, #, #, #, #, #"))
        self.trees.append(Tree("1, 9, #, 9, #, 9, #, 9, #, #, #"))


    def tearDown(self):
        pass


    def testisSame(self):
        for tree in self.trees:
            for secondTree in self.trees:
                if tree == secondTree:
                    self.assertTrue(tree.sameTree(secondTree))
                else:
                    self.assertFalse(tree.sameTree(secondTree))

    def testMaxDepth(self):
        expected = [0, 1, 2, 2, 3, 3, 4, 5]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.maxDepth(), expected[i])

    def testMinDepth(self):
        expected = [0, 1, 1, 1, 2, 3, 3, 1]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.minDepth(), expected[i])

    def testisSymmetric(self):
        expected = [True, True, False, False, False, True, False, False]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.symmetricTree(), expected[i])

    def testisBST(self):
        expected = [True, True, False, True, False, False, True, False]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.bst(), expected[i])

    def testisBalanced(self):
        expected = [True, True, True, True, True, True, True, False]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.balancedTree(), expected[i])

    def testFind(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        tree = BST("5, 3, 7, 2, 4, 6, 8, #, #, #, #, #, #, #, #")
        for value in values:
            self.assertEqual(int(tree.find(value).val), value)

    def testlowestAncestor(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, #, #, #, #, #, #, #, #")
        node2 = tree.find(2)
        node4 = tree.find(5)
        node3 = tree.find(5)
        self.assertEqual(tree.lowestAncestor(node2, node4), node3)

if __name__ == "__main__":
    unittest.main()