class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmpList = []
        while len(nums) > 1:
            tmpList = []
            for i in range(len(nums) - 1):
                tmpList.append((nums[i] + nums[i + 1]) % 10)
            nums = tmpList

        return nums[0]
