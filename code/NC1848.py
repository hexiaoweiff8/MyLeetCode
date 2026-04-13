class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        minDistance = float('inf')
        for i in range(len(nums)):
            if nums[i] == target:
                minDistance = min(minDistance, abs(i - start))
        return minDistance
