class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rightVal = sum(nums)
        leftVal = 0
        for i in range(len(nums)):
            rightVal -= nums[i]
            if leftVal == rightVal:
                return i
            leftVal += nums[i]
        return -1