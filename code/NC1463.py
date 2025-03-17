class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(min(n, i + 1)):
                for k in range(max(j + 1, n - 1 - i), n):
                    dp[i][j + 1][k + 1] = max(
                        dp[i + 1][j][k], dp[i + 1][j][k + 1], dp[i + 1][j][k + 2],
                        dp[i + 1][j + 1][k], dp[i + 1][j + 1][k + 1], dp[i + 1][j + 1][k + 2],
                        dp[i + 1][j + 2][k], dp[i + 1][j + 2][k + 1], dp[i + 1][j + 2][k + 2]
                    ) + grid[i][j] + grid[i][k]
        return dp[0][1][n]

