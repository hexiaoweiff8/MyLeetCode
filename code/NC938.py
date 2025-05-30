# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sumVal = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                sumVal += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return sumVal