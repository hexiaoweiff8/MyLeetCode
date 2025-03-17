class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[[-9999999] * n for _ in range(n)] for _ in range(n * 2 - 1)]
        dp[0][0][0] = grid[0][0]
        for k in range(1, n * 2 - 1):
            for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
                y1 = k - x1
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1, min(k + 1, n)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:
                        continue
                    res = dp[k - 1][x1][x2]
                    if x1:
                        # 往下, 往右
                        res = max(res, dp[k - 1][x1 - 1][x2])
                    if x2:
                        # 往右, 往下
                        res = max(res, dp[k - 1][x1][x2 - 1])
                    if x1 and x2:
                        # 都往下
                        res = max(res, dp[k - 1][x1 - 1][x2 - 1])
                    res += grid[x1][y1]
                    if x1 != x2:
                        # 跳过同一个
                        res += grid[x2][y2]
                    dp[k][x1][x2] = res
        return max(dp[-1][-1][-1], 0)