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

    def maxDepth(self):
        depth = 0
        length = self._maxDepthRecur(self._root, depth)
        return length

    def minDepth(self):
        depth = 0
        length = self._minDepthRecur(self._root, depth)
        return length

if __name__ == "__main__":
    tree = Tree("1, 2, 3, #, #, 4, #, #, #")
    max = tree.maxDepth()
    min = tree.minDepth()
    print(max)
    print(min)