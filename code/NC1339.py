# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            sub_sum.append(s)
            return s

        sub_sum = []
        total = dfs(root)

        ans = max(s * (total - s) for s in sub_sum)
        return ans % (10 ** 9 + 7)