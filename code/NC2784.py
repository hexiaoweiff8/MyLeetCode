import collections


class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxVal = max(nums)
        countVal = collections.Counter(nums)
        for val in range(1, maxVal):
            if countVal[val] != 1:
                return False

        return countVal[maxVal] == 2
