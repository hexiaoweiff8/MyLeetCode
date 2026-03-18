class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 计算左上角矩形前缀和
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(1, n):
                grid[i][j] += grid[i][j - 1]
        for i in range(1, m):
            for j in range(n):
                grid[i][j] += grid[i - 1][j]

        #判断是否存在子矩阵和小于等于k
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] <= k:
                    res += 1

        return res
