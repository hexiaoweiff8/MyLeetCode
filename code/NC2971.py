class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sumVal = sum(nums)
        for index in range(len(nums) - 1, 1, -1):
            if sumVal > nums[index] * 2:
                return sumVal
            sumVal -= nums[index]
        return -1
