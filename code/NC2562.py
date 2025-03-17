class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        i, j = 0, len(nums) - 1
        while i <= j:
            if i != j:
                ret += int(str(nums[i]) + str(nums[j]))
            else:
                ret += nums[i]
            i, j = i + 1, j - 1
        return ret