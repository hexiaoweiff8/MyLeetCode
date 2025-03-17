class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxVal = max(nums)
        return maxVal * k + (k - 1) * k / 2
