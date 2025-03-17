
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ret = []
        node = root
        while stack:
            if node.children:
                if node.children:
                    stack.append(node)
                    node = node.children.pop(0)
            else:
                ret.append(node.val)
                node = stack.pop()

        return ret


obj = Solution()
node = Node(1)
node.children = [Node(3), Node(2), Node(4)]
node.children[0].children = [Node(5), Node(6)]
print(obj.postorder(node))