class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        dis = [[float("inf")] * n for _ in range(m)]
        dis[0][0] = grid[0][0]
        q = [(0, 0)]
        while q:
            i, j = q.pop(0)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]
                    if dis[nx][ny] > dis[i][j] + cost:
                        dis[nx][ny] = dis[i][j] + cost
                        if cost == 0:
                            q.insert(0, (nx, ny))
                        else:
                            q.append((nx, ny))
        return dis[-1][-1] < health