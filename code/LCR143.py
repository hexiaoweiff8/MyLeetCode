# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not B: return False
        def isSameTree(tree1, tree2):
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False
            if tree2.left:
                if not isSameTree(tree1.left, tree2.left):
                    return False
            if tree2.right:
                if not isSameTree(tree1.right, tree2.right):
                    return False
            return True
        stack = []
        stack.append(A)
        while stack:
            node = stack.pop()
            if isSameTree(node, B):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False