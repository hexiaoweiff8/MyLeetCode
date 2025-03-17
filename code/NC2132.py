from itertools import product


class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """

        # existDic = set()
        # n, m = len(grid), len(grid[0])
        # for index, row in enumerate(grid):
        #     for index2, val in enumerate(row):
        #         if val == 0 and (index, index2) not in existDic:
        #             cover = True
        #             for index3 in range(index, min(index + stampHeight, n)):
        #                 if sum(grid[index3][index2: min(index2 + stampWidth, m)]):
        #                     cover = False
        #                     break
        #             if cover:
        #                 for index3 in range(index, index + stampHeight):
        #                     for index4 in range(index2, index2 + stampWidth):
        #                         existDic.add((index, index4))
        #
        # for index, row in enumerate(grid):
        #     for index2, val in enumerate(row):
        #         if val == 0 and (index, index2) not in existDic:
        #             return False
        # return True

        # colPath, rowPath = {}, {}
        # # 组装分段数据
        # for index, row in enumerate(grid):
        #     rowList = []
        #     rowPath[index] = rowList
        #     for index2, val in enumerate(row):
        #         if val == 0:
        #             if rowList:
        #                 startCol, endCol = rowList[-1]
        #                 if index2 - endCol == 1:
        #                     rowList[-1] = (startCol, index2)
        #                 else:
        #                     rowList.append((index2, index2))
        #             else:
        #                 rowList.append((index2, index2))
        #             colList = colPath.get(index2, [])
        #             if colList:
        #                 startRow, endRow = colList[-1]
        #                 if index - endRow == 1:
        #                     colList[-1] = (startRow, index)
        #                 else:
        #                     colList.append((index, index))
        #             else:
        #                 colList.append((index, index))
        #             colPath[index2] = colList
        # print(rowPath)
        # print(colPath)
        # # 判断是否可以全覆盖
        # for row, rowList in rowPath.items():
        #     for colStart, colEnd in rowList:
        #         if colEnd - colStart + 1 < stampWidth:
        #             return False
        #         for col in range(colStart, colEnd + 1):
        #             colList = colPath[col]
        #             for rowStart, rowEnd in colList:
        #                 if rowEnd - rowStart + 1 < stampHeight:
        #                     return False
        def CornerCheck(x, y, dx, dy):
            for i, j in product(range(x + dx, x + dx * stampHeight, dx), range(y + dy, y + dy * stampWidth, dy)):
                if grid[i][j]:
                    return True
            return False

        m, n = len(grid), len(grid[0])
        for i in range(m):
            cnt = 0
            for j in range(n):
                if grid[i][j] and 0 < cnt < stampWidth:
                    return False
                cnt = 0 if grid[i][j] else cnt + 1
            if 0 < cnt < stampWidth:
                return False
        for j in range(n):
            cnt = 0
            for i in range(m):
                if grid[i][j]:
                    if 0 < cnt < stampHeight:
                        return False
                    if cnt and 0 < j < n - 1:
                        if grid[i - 1][j - 1] and CornerCheck(i - 1, j, -1, 1):
                            return False
                        if grid[i - 1][j + 1] and CornerCheck(i - 1, j, -1, -1):
                            return False
                    cnt = 0
                else:
                    cnt += 1
                    if cnt == stampHeight and i >= stampHeight and 0 < j < n - 1:
                        if (grid[i - stampHeight + 1][j - 1]) and CornerCheck(i, j, -1, 1):
                            return False
                        if (grid[i - stampHeight + 1][j + 1]) and CornerCheck(i, j, -1, -1):
                            return False
            if 0 < cnt < stampHeight:
                return False
        return True


obj = Solution()
# print(obj.possibleToStamp([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
#                           stampHeight=4,
#                           stampWidth=3))
# print(obj.possibleToStamp([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], stampHeight=2, stampWidth=2))
#
# print(obj.possibleToStamp([[0, 0, 0, 0, 0],
#                            [0, 0, 0, 0, 0],
#                            [0, 0, 1, 0, 0],
#                            [0, 0, 0, 0, 1],
#                            [0, 0, 0, 1, 1]], stampHeight=2, stampWidth=2))
print(obj.possibleToStamp([[0, 0, 0],
                           [0, 0, 1],
                           [0, 0, 0],
                           [1, 0, 1],
                           [0, 1, 0],
                           [0, 0, 1],
                           [1, 1, 0],
                           [0, 0, 1]],
                          stampHeight=1, stampWidth=1))
print(obj.possibleToStamp([[0, 0, 1, 1],
                           [0, 0, 0, 1],
                           [1, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 1]],
                          stampHeight=2, stampWidth=2))
