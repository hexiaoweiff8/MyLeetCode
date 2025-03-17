class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSum = 0
        for num in nums:
            numSum += num
            while num:
                numSum -= num % 10
                num //= 10
        return numSum