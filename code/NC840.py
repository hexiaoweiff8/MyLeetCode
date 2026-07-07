class Solution(object):
    def numMagicSquaresInside(self, grid):
        padding = 3
        m, n = len(grid[0]), len(grid)
        ans = 0
        if m < 3 or n < 3:
            return 0
        m, n = m - 2, n - 2
        y1Array = [(0, 2), (1, 1), (2, 0)]
        for i in range(n):
            for j in range(m):
                rowVals, colVals = [0, 0, 0], [0, 0, 0]
                x1 = y1 = 0
                for x in range(padding):
                    for y in range(padding):
                        tmpVal = grid[x + i][y + j]
                        rowVals[x] += tmpVal
                        colVals[y] += tmpVal
                        if x == y:
                            x1 += tmpVal
                        if (x, y) in y1Array:
                            y1 += tmpVal
                if colVals[0] == colVals[1] == colVals[2] == rowVals[0] == rowVals[1] == rowVals[2] == x1 == y1:
                    ans += 1

        return ans


obj = Solution()
# print(obj.numMagicSquaresInside([[8]]))
print(obj.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))

