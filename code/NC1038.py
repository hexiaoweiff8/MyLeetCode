# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sortedList = []
        sourceRoot = root
        sumVal = 0
        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            sortedList.append((root.val, root))

        dfs(sourceRoot)
        sortedList = sorted(sortedList, key=lambda x:x[0], reverse=True)
        for i in range(len(sortedList)):
            sumVal += sortedList[i][0]
            sortedList[i][1].val = sumVal
        return root

    def bstToGst2(self, root):
        total = 0
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val += total
                dfs(root.left)
        dfs(root)
        return root


obj = Solution()
tree = TreeNode(4)
tree.left = TreeNode(1)
tree.right = TreeNode(6)

tree.left.left = TreeNode(0)
tree.left.right = TreeNode(2)
tree.left.right.right = TreeNode(3)

tree.right.left = TreeNode(5)
tree.right.right = TreeNode(7)
tree.right.right.right = TreeNode(8)
print(obj.bstToGst(tree))
