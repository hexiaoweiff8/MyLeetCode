class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        size = m * n
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                p = (i * n + j + k) % size
                ans[p // n][p % n] = num

        return ans