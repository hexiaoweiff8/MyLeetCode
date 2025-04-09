class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = set(nums)
        mn = min(nums)
        if k > mn:
            return -1
        res = len(nums)
        if k == mn:
            return res - 1
        return res
