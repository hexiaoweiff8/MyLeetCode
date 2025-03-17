class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        levelDic = {}

        def dfs(node, level):
            if not node:
                return None
            if level not in levelDic:
                levelDic[level] = []
            # 先处理右侧
            if node.right:
                node.right.next = None if not levelDic[level] else levelDic[level][-1]
                levelDic[level].append(node.right)
                dfs(node.right, level + 1)
            if node.left:
                node.left.next = None if not levelDic[level] else levelDic[level][-1]
                levelDic[level].append(node.left)
                dfs(node.left, level + 1)

        dfs(root, 0)
        return root


obj = Solution()
# root = Node(1, Node(2), Node(3))
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.right = Node(7)
# print(obj.connect(root))
# print(obj.connect(Node()))
# [0, 2,4, 1,null, 3,-1, 5,1, null,6,null,8]
root = Node(0, Node(2), Node(4))
root.left = Node(1)
root.right.left = Node(3)
root.right.right = Node(-1)
root.left.left = Node(5)
root.left.right = Node(1)
root.right.left.right = Node(6)
root.right.right.right = Node(8)
print(obj.connect(root))