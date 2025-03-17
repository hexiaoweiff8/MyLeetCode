# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def batchTree(root, mi, ma):
            if root is None:
                return 0
            diff = max(abs(root.val - mi), abs(root.val - ma))
            diff = max(diff, batchTree(root.left, min(mi, root.val), max(ma, root.val)))
            diff = max(diff, batchTree(root.right, min(mi, root.val), max(ma, root.val)))
            return diff

        # 遍历树
        return batchTree(root, root.val, root.val)


root = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
rootNode = TreeNode(root[0])
rootNode.left = TreeNode(root[1])
rootNode.right = TreeNode(root[2])
rootNode.left.left = TreeNode(root[3])
rootNode.left.right = TreeNode(root[4])
# rootNode.right.left = TreeNode(root[5])
rootNode.right.right = TreeNode(root[6])
# rootNode.left.left.left = TreeNode(root[7])
# rootNode.left.left.right = TreeNode(root[8])
rootNode.left.right.left = TreeNode(root[9])
rootNode.left.right.right = TreeNode(root[10])
rootNode.right.right.left = TreeNode(root[11])

# root = [1,None,2,None,0,3]
# rootNode = TreeNode(root[0])
# # rootNode.left = TreeNode(root[1])
# rootNode.right = TreeNode(root[2])
# # rootNode.left.left = TreeNode(root[3])
# rootNode.right.right = TreeNode(root[4])
# rootNode.right.right.left = TreeNode(root[5])
# root = [2,None,0,None,4,None,3,None,1]
# rootNode = TreeNode(root[0])
# # rootNode.left = TreeNode(root[1])
# rootNode.right = TreeNode(root[2])
# # rootNode.left.left = TreeNode(root[3])
# rootNode.right.right = TreeNode(root[4])
# # rootNode.right.left = TreeNode(root[5])
# rootNode.right.right.right = TreeNode(root[6])
# # rootNode.left.left.left = TreeNode(root[7])
# rootNode.right.right.right.right = TreeNode(root[8])
obj = Solution()
print(obj.maxAncestorDiff(rootNode))
