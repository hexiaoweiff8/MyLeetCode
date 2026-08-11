class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumVal = nums[0]
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre + 1 != nums[i]:
                break
            sumVal += nums[i]
            pre = nums[i]
        while sumVal in nums:
            sumVal += 1
        return sumVal



