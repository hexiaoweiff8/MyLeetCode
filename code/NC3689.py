class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 获得最大和最小的位置
        n = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        return (nums[max_index] - nums[min_index]) * k