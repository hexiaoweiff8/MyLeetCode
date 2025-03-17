# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ret = []
        if not to_delete:
            ret.append(root)
            return ret

        def dfs(node, newTree=False):
            needDel = False
            if newTree:
                ret.append(node)
            if node.val in to_delete:
                needDel = True
                if newTree:
                    ret.pop()
            if node.left:
                if dfs(node.left, needDel):
                    node.left = None
            if node.right:
                if dfs(node.right, needDel):
                    node.right = None
            return needDel
        dfs(root, True)
        return ret


obj = Solution()
# tn = TreeNode()
# tn.val = 1
# tn.left = TreeNode()
# tn.left.val = 2
# tn.right = TreeNode()
# tn.right.val = 3
# tn.left.left = TreeNode()
# tn.left.left.val = 4
# tn.left.right = TreeNode()
# tn.left.right.val = 5
# tn.right.left = TreeNode()
# tn.right.left.val = 6
# tn.right.right = TreeNode()
# tn.right.right.val = 7
# print(obj.delNodes(tn, [3, 5]))

# tn = TreeNode()
# tn.val = 1
# tn.left = TreeNode()
# tn.left.val = 2
# tn.left.left = TreeNode()
# tn.left.left.val = 4
# tn.left.right = TreeNode()
# tn.left.right.val = 3
# print(obj.delNodes(tn, [2, 3]))

tn = TreeNode()
tn.val = 1
tn.left = TreeNode()
tn.left.val = 2
tn.right = TreeNode()
tn.right.val = 4
tn.left.right = TreeNode()
tn.left.right.val = 3
print(obj.delNodes(tn, [3]))

# tn = TreeNode()
# tn.val = 1
# tn.left = TreeNode()
# tn.left.val = 2
# tn.right = TreeNode()
# tn.right.val = 3
# tn.right.right = TreeNode()
# tn.right.right.val = 4
# print(obj.delNodes(tn, [2, 1]))
#[[3,null,4]]

tn = TreeNode()
tn.val = 1
tn.right = TreeNode()
tn.right.val = 2
tn.right.left = TreeNode()
tn.right.left.val = 3
tn.right.right = TreeNode()
tn.right.right.val = 5
tn.right.left.right = TreeNode()
tn.right.left.right.val = 4
tn.right.left.right.right = TreeNode()
tn.right.left.right.right.val = 6
print(obj.delNodes(tn, [5, 2, 1]))
#[[3,null,4,null,6]]