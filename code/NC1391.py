class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        DIRS = (
            (),
            ((0, -1), (0, 1)),  # 站在街道 1，可以往左或者往右
            ((-1, 0), (1, 0)),  # 站在街道 2，可以往上或者往下
            ((0, -1), (1, 0)),  # 站在街道 3，可以往左或者往下
            ((0, 1), (1, 0)),  # 站在街道 4，可以往右或者往下
            ((0, -1), (-1, 0)),  # 站在街道 5，可以往左或者往上
            ((0, 1), (-1, 0)),  # 站在街道 6，可以往右或者往上
        )
        vis = [[False] * n for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return True
            vis[x][y] = True
            for dx, dy in DIRS[grid[x][y]]:
                i, j = x + dx, y + dy
                if 0 <= i < m\
                        and 0 <= j < n \
                        and not vis[i][j]\
                        and (-dx, -dy) in DIRS[grid[i][j]]:
                    if dfs(i, j):
                        return True
            return False

        return dfs(0, 0)

obj = Solution()
print(obj.hasValidPath([[1,1,2]]))
