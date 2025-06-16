class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = -1
        minPre = nums[0]
        for i in range(len(nums)):
            maxVal = max(maxVal, nums[i] - minPre)
            minPre = min(minPre, nums[i])

        return maxVal or -1