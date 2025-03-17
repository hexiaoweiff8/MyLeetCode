class Solution(object):
    def sellingWood(self, m, n, prices):
        """
        :type m: int
        :type n: int
        :type prices: List[List[int]]
        :rtype: int
        """
        dic = {(h, w): p for h, w, p in prices}
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dic.get((i, j), 0),
                               max([dp[i][k] + dp[i][j - k] for k in range(1, j)], default=0),
                               max([dp[k][j] + dp[i - k][j] for k in range(1, i)], default=0))

        return dp[m][n]


obj = Solution()
print(obj.sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]]))