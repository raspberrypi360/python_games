'''
Created on Oct 3, 2015

@author: ryan
'''
import collections
from tree import *


class BST(Tree):
    def __init__(self, treeStr):
        super(BST, self).__init__(treeStr)
        bst = self.isBST()
        if not bst:
            print("Not a binary search tree")
            self._root = None

    def find(self, value):
        if self._root == None:
            return None
        else:
            return self._find(value, self._root)

    def lowestAncestor(self, node1, node2):
        if self._root == None:
            return None
        else:
            ancestor = self._lowestAncestorRecur(self._root, node1, node2)
            return ancestor

    def insertNode(self, value):
        if self._root == None:
            self._root = TreeNode(value, None)
        else:
            status = self._insertNodeRecur(self._root, value)
            if not status:
                print("Value already exists")

    def minVal(self):
        if self._root == None:
            return None
        else:
            return self._minValRecur(self._root)

    def maxVal(self):
        if self._root == None:
            return None
        else:
            return self._maxValRecur(self._root)

    def nextVal(self, node):
        if node == None:
            return None
        if node.right != None:
            return self._minValRecur(node.right)
        if node.parent == None:
            return None
        if node == node.parent.left:
            return node.parent
        while node != node.parent.left:
            node = node.parent
            if node.parent == None:
                return None
        return node.parent

    def nextValReverse(self, node):
        if node == None:
            return None
        if node.left != None:
            return self._maxValRecur(node.left)
        if node.parent == None:
            return None
        if node == node.parent.right:
            return node.parent
        while node != node.parent.right:
            node = node.parent
            if node.parent == None:
                return None
        return node.parent

    def ascendingOrder(self):
        value = self.minVal()
        while value != None:
            yield value
            value = self.nextVal(value)

    def descendingOrder(self):
        value = self.maxVal()
        while value != None:
            yield value
            value = self.nextValReverse(value)

    def closestValue(self, value):
        node = self._closestValueRecur(value, self._root)
        node2 = None
        if int(node.val) < value:
            node2 = self.nextVal(node)
        elif int(node.val) > value:
            node2 = self.nextValReverse(node)
        else:
            return int(node.val)
        if node2 != None:
            if abs(value - int(node2.val)) > abs(value - int(node.val)):
                return int(node.val)
            else:
                return int(node2.val)
        return int(node.val)

    def _closestValueRecur(self, value, node):
        child = node
        if value < int(node.val):
            if node.left != None:
                child = self._closestValueRecur(value, node.left)
        elif value > int(node.val):
            if node.right != None:
                child = self._closestValueRecur(value, node.right)
        return child

    def _find(self, value, node):
        val = int(node.val)
        if value == val:
            return node
        if value < val and node.left != None:
            return self._find(value, node.left)
        if value > val and node.right != None:
            return self._find(value, node.right)
        return None

    def _lowestAncestorRecur(self, ancestor, node1, node2):
        if node1 == ancestor or node2 == ancestor:
            return ancestor
        if (node1.val < ancestor.val and node2.val > ancestor.val) or (node1.val > ancestor.val and node2.val < ancestor.val):
            return ancestor
        if node1.val < ancestor.val and node2.val < ancestor.val:
            if ancestor.left != None:
                return self._lowestAncestorRecur(ancestor.left, node1, node2)
        if node1.val > ancestor.val and node2.val > ancestor.val:
            if ancestor.right != None:
                return self._lowestAncestorRecur(ancestor.right, node1, node2)
        return None

    def _insertNodeRecur(self, node, value):
        val = int(node.val)
        if value == val:
            return False
        if value < val:
            if node.left != None:
                status = self._insertNodeRecur(node.left, value)
                if not status:
                    return False
            else:
                node.left = TreeNode(value, node)
                return True
        if value > val:
            if node.right != None:
                status = self._insertNodeRecur(node.right, value)
                if not status:
                    return False
            else:
                node.right = TreeNode(value, node)
                return True
        return True

    def _minValRecur(self, node):
        if node.left != None:
            return self._minValRecur(node.left)
        return node

    def _maxValRecur(self, node):
        if node.right != None:
            return self._maxValRecur(node.right)
        return node