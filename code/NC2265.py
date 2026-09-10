# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        def dfs(node):
            if node is None:
                return 0, 0
            leftSum, leftSize = dfs(node.left)
            rightSum, rightSize = dfs(node.right)
            sumVal = leftSum + rightSum + node.val
            sizeVal = leftSize + rightSize + 1
            if node.val == sumVal // sizeVal:
                nonlocal ans
                ans += 1
            return sumVal, sizeVal
        dfs(root)
        return ans

def list_to_tree(data):
    """
    将层序遍历列表转为二叉树。
    例如：[4,8,5,0,1,None,6]
    """
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        node = queue.popleft()

        # 左子节点
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            queue.append(node.left)
        i += 1

        # 右子节点
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            queue.append(node.right)
        i += 1

    return root
obj = Solution()


print(obj.averageOfSubtree(list_to_tree([4,8,5,0,1,None,6])))