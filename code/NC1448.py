# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = 0

        def dfs(node, maxVal):
            nonlocal ret
            if node.val >= maxVal:
                ret += 1
                maxVal = node.val
            if node.left:
                dfs(node.left, maxVal)
            if node.right:
                dfs(node.right, maxVal)
        dfs(root, -9999999999)
        return ret


obj = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
print(obj.goodNodes(root))

root = TreeNode(3)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
print(obj.goodNodes(root))

root = TreeNode(1)
print(obj.goodNodes(root))

root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(4)
print(obj.goodNodes(root))
