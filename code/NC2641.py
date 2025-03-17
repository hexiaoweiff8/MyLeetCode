# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.sourceVal = 0
class Solution(object):
    def replaceValueInTree(self, root):
        tmpNodeList = nodeList = [root]
        root.val = 0
        while nodeList:
            nodeList = []
            nodeList, tmpNodeList = tmpNodeList, nodeList
            levelSum = 0
            for node in nodeList:
                if node.left:
                    tmpNodeList.append(node.left)
                    levelSum += node.left.val
                if node.right:
                    tmpNodeList.append(node.right)
                    levelSum += node.right.val
            for node in nodeList:
                childSum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = levelSum - childSum
                if node.right:
                    node.right.val = levelSum - childSum
        return root


        #
        # def dfs(node, level):
        #     if node.left:
        #         dfs(node.left, level + 1)
        #     if node.right:
        #         dfs(node.right, level + 1)
        #     if level not in levelDic:
        #         levelDic[level] = []
        #     levelDic[level].append(node.val)
        #     node.sourceVal = node.val
        #
        # def dfs2(node1, node2, level):
        #     if node1.left:
        #         dfs2(node1.left, node1.right, level + 1)
        #     if node1.right:
        #         dfs2(node1.right, node1.left, level + 1)
        #     node1.val = sum(levelDic[level]) - node1.sourceVal - (node2.sourceVal if node2 else 0)
        # dfs(root, 0)
        # dfs2(root, None, 0)
        # return root


obj = Solution()
node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(9)
node.left.left = TreeNode(1)
node.left.right = TreeNode(10)
node.right.right = TreeNode(7)

print(obj.replaceValueInTree(node))