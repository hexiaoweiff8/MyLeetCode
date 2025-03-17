# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, depth):
            val1, valNon1 = dfs(node.left, depth + 1) if node.left else (0, 0)
            val2, valNon2 = dfs(node.right, depth + 1) if node.right else (0, 0)
            return node.val + valNon1 + valNon2, max(val1, valNon1) + max(val2, valNon2)
        return max(dfs(root, 0))


obj = Solution()

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
print(obj.rob(root))

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
print(obj.rob(root))

root = TreeNode(4)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(3)
print(obj.rob(root))
