# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # q = [root]
        # sums = []
        # while q:
        #     sums.append(sum(node.val for node in q))
        #     q = [child for node in q for child in (node.left, node.right) if child]
        # sums.sort(reverse=True)
        # return sums[k - 1] if len(sums) >= k else -1
        q = [root]
        sums = []
        while q:
            sums.append(sum(node.val for node in q))
            q = [child for node in q for child in (node.left, node.right) if child]
        sums.sort(reverse=True)
        return sums[k - 1] if len(sums) >= k else -1