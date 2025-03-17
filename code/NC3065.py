class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            if nums[i] < k:
                ans += 1
        return ans