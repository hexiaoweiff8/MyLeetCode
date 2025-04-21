class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        subMax = upper - lower
        minVal = maxVal = 0
        val = 0
        for i in range(len(differences)):
            # print(val)
            val += differences[i]
            minVal = min(minVal, val)
            maxVal = max(maxVal, val)
            if maxVal - minVal > subMax:
                return 0
        # print(val)
        return (upper - lower) - (maxVal - minVal) + 1


obj = Solution()
# print(obj.numberOfArrays([1, -3, 4], 1, 6))
# print(obj.numberOfArrays([3, -4, 5, 1, -2], -4, 5))
print(obj.numberOfArrays([83702,-5216], -82788, 14602))