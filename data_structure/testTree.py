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
        self.trees.append(Tree(""))
        self.trees.append(Tree("1"))
        self.trees.append(Tree("1, 2"))
        self.trees.append(Tree("1, #, 2"))
        self.trees.append(Tree("1, 2, 3, #, #, 4"))
        self.trees.append(Tree("1, 2, 2, 3, 4, 4, 3"))
        self.trees.append(Tree("5, 3, 7, 2, 4, 6, 8, 1"))
        self.trees.append(Tree("1, 9, #, 9, #, 9, #, 9"))


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
            self.assertEqual(tree.isBST(), expected[i])

    def testisBalanced(self):
        expected = [True, True, True, True, True, True, True, False]
        for i, tree in enumerate(self.trees):
            self.assertEqual(tree.balancedTree(), expected[i])

    def testFind(self):
        values = [5, 3, 7, 2, 4, 6, 8]
        tree = BST("5, 3, 7, 2, 4, 6, 8")
        for value in values:
            self.assertEqual(int(tree.find(value).val), value)

    def testlowestAncestor(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8")
        node2 = tree.find(2)
        node4 = tree.find(5)
        node3 = tree.find(5)
        self.assertEqual(tree.lowestAncestor(node2, node4), node3)

    def testinsertNode(self):
        values = [5, 3, 7, 2, 4, 6, 8, 1]
        expected = ["5, #, #", "5, 3, #, #, #", "5, 3, 7, #, #, #, #", "5, 3, 7, 2, #, #, #, #, #", "5, 3, 7, 2, 4, #, #, #, #, #, #", \
                    "5, 3, 7, 2, 4, 6, #, #, #, #, #, #, #", "5, 3, 7, 2, 4, 6, 8, #, #, #, #, #, #, #, #", \
                    "5, 3, 7, 2, 4, 6, 8, 1, #, #, #, #, #, #, #, #, #"]
        tree = BST("")
        for i, value in enumerate(values):
            tree.insertNode(value)
            treeStr2 = str(tree)
            treeStr = expected[i]
            self.assertEqual(treeStr, treeStr2)

    def testminVal(self):
        values = [5, 7, 3, 2, 4, 6, 8, 1]
        expected = [5, 5, 3, 2, 2, 2, 2, 1]
        tree = BST("")
        for i, value in enumerate(values):
            tree.insertNode(value)
            minVal = int(tree.minVal().val)
            self.assertEqual(minVal, expected[i])

    def testmaxVal(self):
        values = [5, 7, 3, 2, 4, 6, 8, 1]
        expected = [5, 7, 7, 7, 7, 7, 8, 8]
        tree = BST("")
        for i, value in enumerate(values):
            tree.insertNode(value)
            maxVal = int(tree.maxVal().val)
            self.assertEqual(maxVal, expected[i])

    def testnextVal(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, 1")
        minVal = tree.minVal()
        nextVal = tree.nextVal(minVal)
        expected = [2, 3, 4, 5, 6, 7, 8, None]
        i = 0
        while nextVal != None:
            self.assertEqual(int(nextVal.val), expected[i])
            nextVal = tree.nextVal(nextVal)
            i += 1

    def testnextValReverse(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, 1")
        maxVal = tree.maxVal()
        nextVal = tree.nextValReverse(maxVal)
        expected = [7, 6, 5, 4, 3, 2, 1, None]
        i = 0
        while nextVal != None:
            self.assertEqual(int(nextVal.val), expected[i])
            nextVal = tree.nextValReverse(nextVal)
            i += 1

    def testascendingOrder(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.ascendingOrder()
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testdescendingOrder(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.descendingOrder()
        expected = [8, 7, 6, 5, 4, 3, 2, 1]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testinOrder(self):
        tree = Tree("")
        nextVal = tree.inOrderTraverse()
        self.assertEqual(list(nextVal), [])
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.inOrderTraverse()
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testpreOrder(self):
        tree = Tree("")
        nextVal = tree.preOrderTraverse()
        self.assertEqual(list(nextVal), [])
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.preOrderTraverse()
        expected = [5, 3, 2, 1, 4, 7, 6, 8]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testpostOrder(self):
        tree = Tree("")
        nextVal = tree.postOrderTraverse()
        self.assertEqual(list(nextVal), [])
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.postOrderTraverse()
        expected = [1, 2, 4, 3, 6, 8, 7, 5]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testprintPaths(self):
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        expected = [[5, 3, 2, 1], [5, 3, 4], [5, 7, 6], [5, 7, 8]]
        paths = tree.printPaths()
        for i, path in enumerate(paths):
            pathCopy = path[:]
            for j in range(len(pathCopy)):
                pathCopy[j] = int(pathCopy[j].val)
            self.assertEqual(pathCopy, expected[i])

    def testbreathFirst(self):
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        expected = [5, 3, 7, 2, 4, 6, 8, 1]
        nextVal = tree.breathFirst()
        for i, value in enumerate(nextVal):
            self.assertEqual(value, expected[i])

    def testdepthFirst(self):
        tree = Tree("")
        nextVal = tree.depthFirst()
        self.assertEqual(list(nextVal), [])
        tree = Tree("5, 3, 7, 2, 4, 6, 8, 1")
        nextVal = tree.depthFirst()
        expected = [5, 3, 2, 1, 4, 7, 6, 8]
        for i, value in enumerate(nextVal):
            self.assertEqual(int(value.val), expected[i])

    def testclosestValue(self):
        tree = BST("5, 3, 7, 2, 4, 6, 8, 1")
        self.assertEqual(2, tree.closestValue(2.3))
        self.assertEqual(3, tree.closestValue(2.6))
        self.assertEqual(3, tree.closestValue(2.5))
        self.assertEqual(8, tree.closestValue(8.01))
        i = 1
        while i < 8.5:
            self.assertEqual(round(i), tree.closestValue(i))
            i+=0.2
        
if __name__ == "__main__":
    unittest.main()