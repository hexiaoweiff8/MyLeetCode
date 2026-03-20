from itertools import pairwise


class Solution(object):
    def minAbsDiff(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        # 进行卷积操作, 值为窗口中最小绝对差值
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            sub_grid = grid[i:i + k]
            for j in range(n - k + 1):
                tmp_grid = []
                for row in sub_grid:
                    tmp_grid += row[j:j + k]
                tmp_grid.sort()

                res = float('inf')
                for x, y in pairwise(tmp_grid):
                    if x < y:
                        res = min(res, y - x)

                if res < float('inf'):
                    ans[i][j] = res

        return ans

