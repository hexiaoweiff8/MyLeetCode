class Solution(object):
    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        pathDic = {}
        if grid[0][0] != 0:
            return False
        allLen = len(grid) * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                pathDic[grid[row][col]] = (row, col)
        preRow, preCol = pathDic[0]
        for index in range(1, allLen):
            row, col = pathDic[index]
            if abs((preRow - row) * (preCol - col)) != 2:
                return False
            preRow, preCol = row, col
        return True


obj = Solution()
print(obj.checkValidGrid(
    [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]))
print(obj.checkValidGrid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]))
print(obj.checkValidGrid([[24, 11, 22, 17, 4],
                          [21, 16, 5, 12, 9],
                          [6, 23, 10, 3, 18],
                          [15, 20, 1, 8, 13],
                          [0, 7, 14, 19, 2]]))
