class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        negCount = posCount = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                posCount += 1
            elif nums[i] < 0:
                negCount += 1
        return max(posCount, negCount)

