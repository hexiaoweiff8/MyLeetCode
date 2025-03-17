class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        maxDic = {}
        ret = []
        for row in range(n):
            rowList = grid[row]
            for col in range(n - 2):
                maxDic[(row << 8) + col] = max(rowList[col: col + 3])

        for row in range(n - 2):
            rowList = []
            ret.append(rowList)
            for col in range(n - 2):
                rowList.append(
                    max(maxDic[(row << 8) + col], maxDic[((row + 1) << 8) + col], maxDic[((row + 2) << 8) + col]))

        return ret


obj = Solution()
print(obj.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(obj.largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
