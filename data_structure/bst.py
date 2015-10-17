'''
Created on Oct 3, 2015

@author: ryan
'''
import collections
from tree import *

class BST(Tree):
    def __init__(self, treeStr):
        super(BST, self).__init__(treeStr)

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

    def lowestAncestor(self, node1, node2):
        if self._root == None:
            return None
        else:
            ancestor = self._lowestAncestorRecur(self._root, node1, node2)
            return ancestor

    def find(self, value):
        return self._find(value, self._root)