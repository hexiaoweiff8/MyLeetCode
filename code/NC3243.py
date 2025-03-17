class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        pre = [[i - 1] for i in range(n)]
        pre[0] = []
        dp = [i for i in range(n)]
        ans = []
        for (x, y) in queries:
            pre[y].append(x)
            for v in range(y, n):
                for u in pre[v]:
                    dp[v] = min(dp[v], dp[u] + 1)
            ans.append(dp[-1])
        return ans


obj = Solution()
print(obj.shortestDistanceAfterQueries(n=5, queries=[[2, 4], [0, 2], [0, 4]]))
