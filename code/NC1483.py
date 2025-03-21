class TreeAncestor(object):

    def __init__(self, n, parent):
        """
        :type n: int
        :type parent: List[int]
        """
        self.log = 16
        self.ancestors = [[-1] * self.log for _ in range(n)]
        for i in range(n):
            self.ancestors[i][0] = parent[i]
        for j in range(1, self.log):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def getKthAncestor(self, node, k):
        """
        :type node: int
        :type k: int
        :rtype: int
        """
        for j in range(self.log):
            if (k >> j) & 1:
                node = self.ancestors[node][j]
                if node == -1:
                    return -1
        return node



# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)