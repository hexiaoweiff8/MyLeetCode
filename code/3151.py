class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        preNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] % 2 == preNum % 2:
                return False
            preNum = nums[i]
        return True
