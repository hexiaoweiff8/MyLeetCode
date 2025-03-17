# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        if root is None:
            return 0
        res = 0
        preStack, stack = [None], [root]
        dic = {}
        preNode = None
        while stack:
            tmpList = stack
            stack = []
            for node in tmpList:
                nextList = []
                dic[node.val] = {"node": node, "next": nextList, "pre": preNode}
                if node.left:
                    stack.append(node.left)
                    nextList.append(node.left)
                    preStack.append(node)
                if node.right:
                    stack.append(node.right)
                    nextList.append(node.right)
                    preStack.append(node)
                dic[node.val]["pre"] = preStack.pop(0) if preStack else None
        stack = [dic[start]]
        del dic[start]
        while stack:
            tmpList = stack
            stack = []
            for node in tmpList:
                if node["next"]:
                    for n in node["next"]:
                        if n.val in dic:
                            stack.append(dic[n.val])
                            del dic[n.val]
                if node["pre"] and node["pre"].val in dic:
                    stack.append(dic[node["pre"].val])
                    del dic[node["pre"].val]
            res += 1
        return res - 1

obj = Solution()
node = TreeNode(1)
node.left = TreeNode(5)
node.right = TreeNode(3)
node.left.right = TreeNode(4)
node.left.right.left = TreeNode(9)
node.left.right.right = TreeNode(2)
node.right.left = TreeNode(10)
node.right.right = TreeNode(6)
print(obj.amountOfTime(node, 3))

node = TreeNode(2)
node.left = TreeNode(5)
print(obj.amountOfTime(node, 5))

node = TreeNode(4)
node.left = TreeNode(5)
node.left.left = TreeNode(3)
node.left.right = TreeNode(2)
print(obj.amountOfTime(node, 3))

node = TreeNode(4)
node.left = TreeNode(3)
node.right = TreeNode(1)
node.left.right = TreeNode(5)
node.right.right = TreeNode(2)

print(obj.amountOfTime(node, 5))