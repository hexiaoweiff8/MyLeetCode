from collections import defaultdict


class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        res = [-1, -1]
        dic = defaultdict(bool)
        for i in range(n):
            for j in range(n):
                if dic.get(grid[i][j], False):
                    res[0] = grid[i][j]
                dic[grid[i][j]] = True
        for v in range(1, n * n + 1):
            if not dic.get(v, False):
                res[1] = v
        return res