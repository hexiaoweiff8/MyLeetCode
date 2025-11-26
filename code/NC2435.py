class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(m):
            for j in range(n):
                for t in range(k):
                    if i > 0:
                        dp[i][j][(t + grid[i][j]) % k] += dp[i - 1][j][t]
                    if j > 0:
                        dp[i][j][(t + grid[i][j]) % k] += dp[i][j - 1][t]
        return dp[m - 1][n - 1][0] % (10 ** 9 + 7)
