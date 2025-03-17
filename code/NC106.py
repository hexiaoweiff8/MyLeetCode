# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        map = {}

        def buildTree(start1, end1, start2, end2):
            if end1 < start1 or end2 < start2:
                return None
            root = postorder[end2]
            rootIndex = map[root]

            node = TreeNode(root)
            node.left = buildTree(start1, rootIndex - 1, start2, start2 + (rootIndex - 1 - start1))
            node.right = buildTree(rootIndex + 1, end1, start2 + rootIndex - start1, end2 - 1)
            return node
        for i in range(len(inorder)):
            map[inorder[i]] = i
        root = buildTree(0, len(inorder) - 1, 0, len(postorder) - 1)
        return root
