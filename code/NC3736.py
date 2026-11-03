class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxV = max(nums)
        return sum([maxV - x for x in nums])
