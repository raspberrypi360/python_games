'''
Created on Apr 3, 2015

@author: ryan
'''
import unittest
from tree import *


class Test(unittest.TestCase):


    def setUp(self):
        self.trees = []
        self.trees.append(Tree("#"))
        self.trees.append(Tree("1, #, #"))
        self.trees.append(Tree("1, 2, #, #, #"))
        self.trees.append(Tree("1, #, 2, #, #"))
        self.trees.append(Tree("1, 2, 3, #, #, 4, #, #, #"))
        self.trees.append(Tree("1, 2, 2, 3, 4, 4, 3, #, #, #, #, #, #, #, #"))


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
        expected = [0, 1, 2, 2, 3, 3]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.maxDepth(), expected[i])

    def testMinDepth(self):
        expected = [0, 1, 1, 1, 2, 3]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.minDepth(), expected[i])

    def testisSymmetric(self):
        expected = [True, True, False, False, False, True]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.symmetricTree(), expected[i])
            
if __name__ == "__main__":
    unittest.main()