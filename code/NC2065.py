class Solution(object):
    def maximalPathQuality(self, values, edges, maxTime):
        """
        :type values: List[int]
        :type edges: List[List[int]]
        :type maxTime: int
        :rtype: int
        """
        n = len(values)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
        dp = [[0] * (maxTime + 1) for _ in range(n)]
        def dfs(node):
            if dp[node][0]:
                return dp[node]
            res = [0] * (maxTime + 1)
            for child in g[node]:
                child_res = dfs(child)
                for i in range(maxTime + 1):
                    res[i] = max(res[i], values[node] + child_res[min(i + 1, maxTime)])
            dp[node] = res

        return max(dfs(0))

