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

    def __str__(self):
        return self.val

class Tree(object):
    def __init__(self, treeStr):
        self._root = None
        if not (treeStr == None or len(treeStr) == 0):
            self.treeStr = treeStr.split(", ")
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

    def isBST(self):
        if self._root == None:
            return True
        else:
            bst, minVal = self._bstRecur(self._root, True)
            return bst

    def balancedTree(self):
        if self._root == None:
            return True
        else:
            balanced, maxVal = self._balancedTreeRecur(self._root)
            return balanced

    def inOrderTraverse(self):
        return self._inOrderTraverse(self._root)

    def preOrderTraverse(self):
        return self._preOrderTraverse(self._root)

    def postOrderTraverse(self):
        return self._postOrderTraverse(self._root)

    def breathFirst(self):
        if self._root != None:
            deque = collections.deque()
            deque.append(self._root)
            while len(deque) != 0:
                node = deque.popleft()
                yield int(node.val)
                if node.left != None:
                    deque.append(node.left)
                if node.right != None:
                    deque.append(node.right)

    def printPaths(self):
        return self._printPaths(self._root, [])

    def depthFirst(self):
        return self._preOrderTraverse(self._root)

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
            if index >= len(self.treeStr):
                break
            if self.treeStr[index] != "#":
                node = TreeNode(self.treeStr[index], parent)
                queue.append(node)
                parent.left = node
            index += 1
            if index >= len(self.treeStr):
                break
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

    def _bstRecur(self, node, minRet):
        retVal = node.val
        if node.left == None and node.right == None:
            return True, node.val
        if node.left != None:
            bst, maxVal = self._bstRecur(node.left, False)
            if not bst or maxVal >= node.val:
                return False, node.val
            if minRet:
                retVal = maxVal
        if node.right != None:
            bst, minVal = self._bstRecur(node.right, True)
            if not bst or minVal <= node.val:
                return False, node.val
            if not minRet:
                retVal = minVal
        return True, retVal

    def _balancedTreeRecur(self, node):
        leftHeight = 0
        rightHeight = 0
        if node.left == None and node.right == None:
            return True, 1
        if node.left != None:
            balanced, leftHeight = self._balancedTreeRecur(node.left)
            if balanced == False:
                return False, 1
        if node.right != None:
            balanced, rightHeight = self._balancedTreeRecur(node.right)
            if balanced == False:
                return False, 1
        if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
            return False, 1
        return True, max(leftHeight, rightHeight) + 1

    def _inOrderTraverse(self, node):
        if node == None:
            return
        if node.left != None:
            yield from self._inOrderTraverse(node.left)
        yield node
        if node.right != None:
            yield from self._inOrderTraverse(node.right)

    def _preOrderTraverse(self, node):
        if node == None:
            return
        yield node
        if node.left != None:
            yield from self._preOrderTraverse(node.left)
        if node.right != None:
            yield from self._preOrderTraverse(node.right)

    def _postOrderTraverse(self, node):
        if node == None:
            return
        if node.left != None:
            yield from self._postOrderTraverse(node.left)
        if node.right != None:
            yield from self._postOrderTraverse(node.right)
        yield node

    def _printPaths(self, node, path):
        if node == None:
            return
        path.append(node)
        if node.left != None:
            yield from self._printPaths(node.left, path)
            path.remove(node.left)
        if node.right != None:
            yield from self._printPaths(node.right, path)
            path.remove(node.right)
        if node.right == None and node.left == None:
            yield path