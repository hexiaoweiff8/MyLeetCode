class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pMax, nMin = 0, 0
        pSum, nSum = 0, 0
        for n in nums:
            pSum += n
            pMax = max(pMax, pSum)
            pSum = max(0, pSum)
            nSum += n
            nMin = min(nMin, nSum)
            nSum = min(0, nSum)
        return max(pMax, -nMin)


obj = Solution()
print(obj.maxAbsoluteSum([1, -3, 2, 3, -4]))
print(obj.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))
