class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        # 获取长度
        borderLen = len(grid)
        maxIndex = borderLen - 1
        for y in range(borderLen):
            row = grid[y]
            for x in range(borderLen):
                val = row[x]
                if x == y or x + y == maxIndex:
                    if val == 0:
                        return False
                else:
                    if val != 0:
                        return False
        return True

obj = Solution()
print(obj.checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))