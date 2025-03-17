class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[0] * n for _ in range(n + 1)]
        for i, row in enumerate(grid, 1):
            for j, val in enumerate(row):
                x = min([dp[i - 1][k] for k in range(n) if k != j], default=0)
                dp[i][j] = val + x
        return min(dp[n])


obj = Solution()
print(obj.minFallingPathSum(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
