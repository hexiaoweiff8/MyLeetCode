# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ret = []

        def dfs(node):
            if node:
                ret.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                ret.append('#')
        dfs(root)
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        args = data.split(',')

        def dfs(arg):
            val = next(arg)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs(arg)
            node.right = dfs(arg)
            return node
        return dfs(args.__iter__())


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
tree = ser.serialize(root)
ans = deser.deserialize(tree)
print(ans)
# return ans