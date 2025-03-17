class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        for i in range(0, n):
            if sum(grid[i]) == n - 1:
                return i