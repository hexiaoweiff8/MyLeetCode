class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 找到起点以及统计所有0点数量
        r, c = len(grid), len(grid[0])
        si = sj = n = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    n += 1
                elif grid[i][j] == 1:
                    n += 1
                    si, sj = i, j

        def dfs(i, j, n):
            if grid[i][j] == 2:
                if n == 0:
                    return 1
                return 0
            t = grid[i][j]
            grid[i][j] = -1
            res = 0
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] in [0, 2]:
                    res += dfs(ni, nj, n - 1)
            grid[i][j] = t
            return res

        return dfs(si, sj, n)


obj = Solution()
print(obj.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print(obj.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
