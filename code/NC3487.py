class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        nums_set = set(nums)
        sum_val = sum([num if num > 0 else 0 for num in nums_set])
        if sum_val == 0:
            return max(nums)
        return sum([num if num > 0 else 0 for num in nums_set])