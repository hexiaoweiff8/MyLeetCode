class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        colSumLen = len(colSum)
        rowSumLen = len(rowSum)
        ret = [[0] * colSumLen for _ in range(rowSumLen)]
        # 确定每个位置最大值
        for col, colVal in enumerate(colSum):
            for row, rowVal in enumerate(rowSum):
                ret[row][col] = x = min(colVal, rowSum[row])
                colVal -= x
                rowSum[row] -= x

        return ret


obj = Solution()
print(obj.restoreMatrix([3, 8], [4, 7]))
