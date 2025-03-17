class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        # 确定四个方向边界
        xMin, xMax = 0, max(queens, key=lambda x: x[0])[0]
        yMin, yMax = 0, max(queens, key=lambda x: x[1])[1]
        dirDic = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        # king向八个方向延伸
        maxRange = max(king[0], xMax - king[0], king[1], yMax - king[1]) + 1
        for idx, dirVal in enumerate(dirDic):
            for index in range(maxRange):
                xVal, yVal = king[0] + dirVal[0] * index, king[1] + dirVal[1] * index
                if xMin <= xVal <= xMax and yMin <= yVal <= yMax and [xVal, yVal] in queens:
                    ret.append([xVal, yVal])
                    break
        return ret


obj = Solution()
# print(obj.queensAttacktheKing(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0]))
# print(obj.queensAttacktheKing(queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]))
# print(obj.queensAttacktheKing(
#     queens=[[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4],
#             [2, 2], [1, 1], [6, 4], [5, 4], [0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2],
#             [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]], king=[3, 4]))
print(obj.queensAttacktheKing(queens=[[0, 0]], king=[7, 7]))
