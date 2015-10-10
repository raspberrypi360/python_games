'''
Created on Oct 3, 2015

@author: ryan
'''
import collections

class TreeNode(object):
    def __init__(self, x, parent):
        self.val = x
        self.parent = parent
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, treeStr):
        self.treeStr = treeStr.split(", ")
        self._root = None
        self._buildTree()
    
    def __str__(self):
        final = ""
        fqueue = collections.deque()
        fqueue.append(self._root)
        while fqueue:
            parent = fqueue.popleft()
            if parent == None:
                final += "#"
                if len(fqueue) != 0:
                    final += ", "
            else:
                final += str(parent.val)
                final += ", "
                fqueue.append(parent.left)
                fqueue.append(parent.right)
        return final

    def _buildTree(self):
        if self.treeStr[0] == "#":
            return
        queue = collections.deque()
        self._root = TreeNode(self.treeStr[0], None)
        index = 0
        queue.append(self._root)
        while queue:
            parent = queue.popleft()
            index += 1
            if self.treeStr[index] != "#":
                node = TreeNode(self.treeStr[index], parent)
                queue.append(node)
                parent.left = node
            index += 1
            if self.treeStr[index] != "#":
                node = TreeNode(self.treeStr[index], parent)
                queue.append(node)
                parent.right = node
    
    def _maxDepthRecur(self, node, depth):
        if node == None:
            return depth
        depth += 1
        lengthL = self._maxDepthRecur(node.left, depth)
        lengthR = self._maxDepthRecur(node.right, depth)
        return max(lengthL, lengthR)

    def _minDepthRecur(self, node, depth):
        if node == None:
            return depth
        depth += 1
        lengthL = self._minDepthRecur(node.left, depth)
        lengthR = self._minDepthRecur(node.right, depth)
        return min(lengthL, lengthR)
    
    def _sameTreeRecur(self, node1, node2):
        if node1.val != node2.val:
            return False
        if (node1.left != None and node2.left == None) or (node1.left == None and node2.left != None):
            return False
        if (node1.right != None and node2.right == None) or (node1.right == None and node2.right != None):
            return False
        if node1.left != None and node2.left != None:
            leftComp = self._sameTreeRecur(node1.left, node2.left)
            if leftComp == False:
                return False
        if node1.right != None and node2.right != None:
            rightComp = self._sameTreeRecur(node1.right, node2.right)
            return rightComp
        return True

    def _symmetricTreeRecur(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 != None and node2 == None:
            return False
        if node1 == None and node2 != None:
            return False
        if node1.val != node2.val:
            return False
        comp1 = self._symmetricTreeRecur(node1.left, node2.right)
        if comp1 == False:
            return False
        comp2 = self._symmetricTreeRecur(node1.right, node2.left)
        return comp2

    def maxDepth(self):
        depth = 0
        length = self._maxDepthRecur(self._root, depth)
        return length

    def minDepth(self):
        depth = 0
        length = self._minDepthRecur(self._root, depth)
        return length
    
    def sameTree(self, tree):
        if self._root != None and tree._root != None:
            return self._sameTreeRecur(self._root, tree._root)
        elif self._root != None and tree._root == None:
            return False
        elif self._root == None and tree._root != None:
            return False
        else:
            return True

    def symmetricTree(self):
        if self._root == None:
            return True
        else:
            return self._symmetricTreeRecur(self._root.left, self._root.right)