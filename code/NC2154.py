
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        cnt = set(nums)
        while original in cnt:
            original *= 2
        return original