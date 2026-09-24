class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            sumV = 0
            while num:
                sumV += num % 10
                num //= 10
            if sumV == i:
                return i
        return -1