# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        # 遍历树
        def dfs(node, val=0):
            needDel = 0
            if node.left:
                if dfs(node.left, val + node.val):
                    node.left = None
                    needDel += 1
                else:
                    needDel -= 1
            if node.right:
                if dfs(node.right, val + node.val):
                    node.right = None
                    needDel += 1
                else:
                    needDel -= 1

            if needDel > 0:
                return True
            if not node.left and not node.right:
                return val + node.val < limit
            else:
                return False
        if dfs(root):
            root = None
        return root


obj = Solution()
# node = TreeNode()
# node.val = 1
# node.left = TreeNode()
# node.left.val = 2
# node.right = TreeNode()
# node.right.val = 3
#
# node.left.left = TreeNode()
# node.left.left.val = 4
# node.left.right = TreeNode()
# node.left.right.val = -99
#
# node.right.left = TreeNode()
# node.right.left.val = -99
# node.right.right = TreeNode()
# node.right.right.val = 7
#
# node.left.left.left = TreeNode()
# node.left.left.left.val = 8
# node.left.left.right = TreeNode()
# node.left.left.right.val = 9
# node.left.right.left = TreeNode()
# node.left.right.left.val = -99
# node.left.right.right = TreeNode()
# node.left.right.right.val = -99
#
# node.right.left.left = TreeNode()
# node.right.left.left.val = 12
# node.right.left.right = TreeNode()
# node.right.left.right.val = 13
# node.right.right.left = TreeNode()
# node.right.right.left.val = -99
# node.right.right.right = TreeNode()
# node.right.right.right.val = 14
# print(obj.sufficientSubset(node, 1))

# node = TreeNode()
# node.val = 5
# node.left = TreeNode()
# node.left.val = 4
# node.right = TreeNode()
# node.right.val = 8
#
# node.left.left = TreeNode()
# node.left.left.val = 11
#
# node.right.left = TreeNode()
# node.right.left.val = 17
# node.right.right = TreeNode()
# node.right.right.val = 4
#
# node.left.left.left = TreeNode()
# node.left.left.left.val = 7
# node.left.left.right = TreeNode()
# node.left.left.right.val = 1
#
# node.right.right.left = TreeNode()
# node.right.right.left.val = 5
# node.right.right.right = TreeNode()
# node.right.right.right.val = 3
# print(obj.sufficientSubset(node, 22))
# [1,2,-3,-5,null,4,null]
# -1

# node = TreeNode()
# node.val = 1
# node.left = TreeNode()
# node.left.val = 2
# node.right = TreeNode()
# node.right.val = -3
#
# node.left.left = TreeNode()
# node.left.left.val = -5
#
# node.right.left = TreeNode()
# node.right.left.val = 4
# print(obj.sufficientSubset(node, -1))

node = TreeNode()
node.val = 10
node.left = TreeNode()
node.left.val = 5
node.right = TreeNode()
node.right.val = 10
print(obj.sufficientSubset(node, 21))