class Solution(object):
    def numberOfRightTriangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        rowCount = [0] * len(grid)
        colCount = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowCount[i] += grid[i][j]
                colCount[j] += grid[i][j]

        for i in range(len(grid)):
            if rowCount[i] > 1:
                for j in range(len(grid[0])):
                    if grid[i][j] > 0 and colCount[j] > 1:
                        ret += (rowCount[i] - 1) * (colCount[j] - 1)

        return ret
