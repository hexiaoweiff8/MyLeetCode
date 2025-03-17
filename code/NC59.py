class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = 0
        for i in range(1, n * n + 1):
            res[x][y] = i
            nx, ny = x + dirs[dir][0], y + dirs[dir][1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or res[nx][ny] != 0:
                dir = (dir + 1) % 4
                nx, ny = x + dirs[dir][0], y + dirs[dir][1]
            x, y = nx, ny
            if x < 0 or x >= n or y < 0 or y >= n or res[x][y] != 0:
                break
                dir = (dir + 1) % 4
                nx, ny = x + dirs[dir][0], y + dirs[dir][1]
                x, y = nx, ny
        return res