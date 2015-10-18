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

    def lowestAncestor(self, node1, node2):
        if self._root == None:
            return None
        else:
            ancestor = self._lowestAncestorRecur(self._root, node1, node2)
            return ancestor

    def find(self, value):
        if self._root == None:
            return None
        else:
            return self._find(value, self._root)

    def insertNode(self, value):
        if self._root == None:
            self._root = TreeNode(value, None)
        else:
            status = self._insertNodeRecur(self._root, value)
            if not status:
                print("Value already exists")