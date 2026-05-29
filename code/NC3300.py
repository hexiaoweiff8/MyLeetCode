class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = 9999999
        for num in nums:
            val = 0
            while num > 0:
                val += num % 10
                num //= 10
            minVal = min(minVal, val)

        return minVal