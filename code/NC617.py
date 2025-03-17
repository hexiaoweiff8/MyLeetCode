# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        ret = root1
        if not root1:
            return root2
        if not root2:
            return root1

        def dfs(node1, node2):
            if node1.left and node2.left:
                node1.left.val += node2.left.val
                dfs(node1.left, node2.left)
            elif node2.left:
                node1.left = node2.left
            if node1.right and node2.right:
                node1.right.val += node2.right.val
                dfs(node1.right, node2.right)
            elif node2.right:
                node1.right = node2.right
        root1.val += root2.val
        dfs(root1, root2)
        return ret


obj = Solution()
tree1 = TreeNode(1)
tree2 = TreeNode(2)
tree1.left = TreeNode(3)
tree1.right = TreeNode(2)
tree1.left.left = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(3)
tree2.left.right = TreeNode(4)
tree2.right.right = TreeNode(7)
print(obj.mergeTrees(tree1, tree2))
