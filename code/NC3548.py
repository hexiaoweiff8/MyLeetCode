class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        # 求左上角矩形的前缀和
        preSum = [[0 for _ in range(n)] for _ in range(m)]
        preSum[0][0] = grid[0][0]
        for i in range(1, m):
            preSum[i][0] = preSum[i - 1][0] + grid[i][0]
        for j in range(1, n):
            preSum[0][j] = preSum[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                preSum[i][j] = preSum[i - 1][j] + preSum[i][j - 1] - preSum[i - 1][j - 1] + grid[i][j]



