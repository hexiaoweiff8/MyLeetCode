class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        for index in range(len(nums)):
            if index.bit_count() == k:
               ret += nums[index]
        return ret