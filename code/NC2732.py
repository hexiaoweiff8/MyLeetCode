class Solution(object):
    def goodSubsetofBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        cnt = [0] * m
        for j in range(n):
            for i in range(m):
                if grid[i][j]:
                    cnt[i] += 1

        for i in range(m):
            if cnt[i] == n:
                return [i + 1]

        return []