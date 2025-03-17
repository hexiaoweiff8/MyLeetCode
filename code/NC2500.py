class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in zip(*grid):
            print(i)
        zipItem = zip(*grid)
        print(zip(*grid))
        for i in grid:
            i.sort()
        return sum([max(i) for i in zip(*grid)])
        # ret = 0
        # while grid[0]:
        #     maxItem = 0
        #     for row in grid:
        #         rowMax = max(row)
        #         maxItem = max(maxItem, rowMax)
        #         row.remove(rowMax)
        #     ret += maxItem
        #
        # return ret


obj = Solution()
print(obj.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]))
print(obj.deleteGreatestValue([[10]]))
