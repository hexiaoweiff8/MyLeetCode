# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0
        def dfs(node):
            if node is None:
                return 0
            d = dfs(node.left) + dfs(node.right) + node.val - 1
            nonlocal ret
            ret += abs(d)
            return d
        dfs(root)
        return ret


obj = Solution()
root = TreeNode()
root.val = 3
root.left = TreeNode()
root.right = TreeNode()
print(obj.distributeCoins(root))

root = TreeNode()
root.val = 0
root.left = TreeNode()
root.right = TreeNode()
root.left.val = 3
root.right.val = 0
print(obj.distributeCoins(root))

root = TreeNode()
root.val = 1
root.left = TreeNode()
root.right = TreeNode()
root.left.val = 0
root.right.val = 2
print(obj.distributeCoins(root))

root = TreeNode()
root.val = 1
root.left = TreeNode()
root.right = TreeNode()
root.left.val = 0
root.right.val = 0
root.left.right = TreeNode()
root.left.right.val = 3
print(obj.distributeCoins(root))
