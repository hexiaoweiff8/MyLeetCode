class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preNum = nums[0]
        ret = 0
        for index, num in enumerate(nums):
            if preNum > num:
                break
            preNum = num
            ret = index
        return ret


obj = Solution()
print(obj.findPeakElement([1, 2, 3, 1]))
