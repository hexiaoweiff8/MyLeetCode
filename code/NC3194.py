class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums.sort()
        ret = 99999999
        while nums:
            ret = min(ret, float(nums.pop(0) + nums.pop()) / 2)
        return ret