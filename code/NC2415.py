# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 广度优先遍历
        queue = [root]
        level = 0
        while queue:
            if level % 2 == 1:
                for i in range(len(queue) // 2):
                    node1, node2 = queue[i], queue[len(queue) - i - 1]
                    node1.val, node2.val = node2.val, node1.val
            queue, tmpQueue = [], queue
            for node in tmpQueue:
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            level += 1
        return root


obj = Solution()
root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)
print(obj.reverseOddLevels(root))
