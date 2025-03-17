class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = res = 0
        for i, num in enumerate(nums):
            while num - nums[left] > k * 2:
                left += 1
            res = max(res, i - left + 1)
        return res