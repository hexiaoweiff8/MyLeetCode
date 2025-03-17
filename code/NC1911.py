class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even, odd = nums[0], 0
        for i in range(1, len(nums)):
            even, odd = max(even, odd + nums[i]), max(odd, even - nums[i])
        return even


obj = Solution()
print(obj.maxAlternatingSum([4, 2, 5, 3]))
