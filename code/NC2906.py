class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(grid), len(grid[0])
        allMutl = 1
        res = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                res[i][j] = allMutl
                allMutl = allMutl * grid[i][j] % 12345

        pre = 1
        for i in range(n):
            for j in range(m):
                res[i][j] = res[i][j] * pre % 12345
                pre = pre * grid[i][j] % 12345
        return res
