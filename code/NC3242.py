class NeighborSum(object):

    def __init__(self, grid):
        """
        :type grid: List[List[int]]
        """
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.adjacentSumGrid = [[0] * self.col for _ in range(self.row)]
        self.diagonalSumGrid = [[0] * self.col for _ in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if i > 0: # 左
                    self.adjacentSumGrid[i][j] += self.grid[i - 1][j]
                if i < self.row - 1: # 右
                    self.adjacentSumGrid[i][j] += self.grid[i + 1][j]
                if j > 0: # 上
                    self.adjacentSumGrid[i][j] += self.grid[i][j - 1]
                if j < self.col - 1: # 下
                    self.adjacentSumGrid[i][j] += self.grid[i][j + 1]
                if i > 0 and j > 0: # 左上
                    self.diagonalSumGrid[i][j] += self.grid[i - 1][j - 1]
                if i < self.row - 1 and j < self.col - 1: # 右下
                    self.diagonalSumGrid[i][j] += self.grid[i + 1][j + 1]
                if i < self.row - 1 and j > 0: # 左下
                    self.diagonalSumGrid[i][j] += self.grid[i + 1][j - 1]
                if i > 0 and j < self.col - 1: # 右上
                    self.diagonalSumGrid[i][j] += self.grid[i - 1][j + 1]
        print(self.adjacentSumGrid)
        print(self.diagonalSumGrid)
    def adjacentSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        sumVal = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == value:
                    sumVal += self.adjacentSumGrid[i][j]
        return sumVal


    def diagonalSum(self, value):
        """
        :type value: int
        :rtype: int
        """
        sumVal = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.grid[i][j] == value:
                    sumVal += self.diagonalSumGrid[i][j]
        return sumVal



# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)