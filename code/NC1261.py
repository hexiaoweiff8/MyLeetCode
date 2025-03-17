# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements(object):

    def __init__(self, root):
        def dfs(node, val):
            if node:
                self.set.add(val)
                dfs(node.left, val * 2 + 1)
                dfs(node.right, val * 2 + 2)
        self.set = set()
        dfs(root, 0)

    def find(self, target):
        return target in self.set

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)