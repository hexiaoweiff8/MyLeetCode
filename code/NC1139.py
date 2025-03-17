class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.rows = len(grid)
        self.cols = len(grid[0])
        existScope = set()
        ret = 0
        # 扩散算法
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1 and (row << 10) + col not in existScope:
                    # 获取所有相连1的index
                    scope = self.getAllContact1Index(grid, row, col, self.rows, self.cols)
                    # 处理范围内最大正方形
                    val = self.checkMaxCube(scope, row, col)
                    if val > ret:
                        ret = val
                    existScope = existScope.union(scope)

        return ret * ret

    def getAllContact1Index(self, grid, row, col, maxRow, maxCol):
        ret = set()
        # 只获取右和下为1的index列表
        if col + 1 < maxCol and grid[row][col + 1]:
            ret = ret.union(self.getAllContact1Index(grid, row, col + 1, maxRow, maxCol))
        if row + 1 < maxRow and grid[row + 1][col]:
            ret = ret.union(self.getAllContact1Index(grid, row + 1, col, maxRow, maxCol))
        if grid[row][col]:
            ret.add((row << 10) + col)
        return ret

    # 检测最大正方形
    def checkMaxCube(self, scope, row, col):
        if scope:
            if len(scope) == 1:
                return 1
            else:
                if (row << 10) + col not in scope:
                    return 0
                # 枚举边长
                maxBorder = min(self.rows, self.cols)
                hasNext = True
                while maxBorder > 0:
                    # 上边
                    startRow = row << 10
                    for index in range(maxBorder + 1):
                        if startRow + col + index not in scope:
                            hasNext = False
                            break
                    if hasNext:
                        # 下边
                        downStartRow = (row + maxBorder) << 10
                        for index in range(maxBorder + 1):
                            if downStartRow + col + index not in scope:
                                hasNext = False
                    if hasNext:
                        # 左边
                        for index in range(maxBorder + 1):
                            if ((row + index) << 10) + col not in scope:
                                hasNext = False
                    if hasNext:
                        # 右边
                        for index in range(maxBorder + 1):
                            if ((row + index) << 10) + col + maxBorder not in scope:
                                hasNext = False
                    if hasNext:
                        break
                    hasNext = True
                    maxBorder -= 1
                return max(maxBorder + 1, self.checkMaxCube(scope, row + 1, col), self.checkMaxCube(scope, row, col + 1))


obj = Solution()
# print(obj.largest1BorderedSquare([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(obj.largest1BorderedSquare([[1, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1]]))

# print(obj.getAllContact1Index([[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1]], 0, 0, 3, 4))
