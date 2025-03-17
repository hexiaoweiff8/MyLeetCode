# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ret = None
        maxDepth = -1
        def dfs(node, depth):
            nonlocal ret, maxDepth
            if not node:
                maxDepth = max(maxDepth, depth)
                return depth
            leftDepth = dfs(node.left, depth + 1)
            rightDepth = dfs(node.right, depth + 1)
            if leftDepth == rightDepth == maxDepth:
                ret = node
            return max(leftDepth, rightDepth)
        dfs(root, 0)
        return ret
