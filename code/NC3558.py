class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(node, fa):
            d = 0
            for v in g[node]:
                if v != fa:
                    d = max(d, dfs(v, node) + 1)
            return d

        k = dfs(1, 0)
        return pow(2, k - 1, 1000000007)