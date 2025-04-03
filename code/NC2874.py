class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLeft = [0] * len(nums)
        maxRight = [0] * len(nums)
        maxLeft[0] = nums[0]
        for i in range(1, len(nums)):
            maxLeft[i] = max(maxLeft[i - 1], nums[i])
        maxRight[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], nums[i])
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, (maxLeft[i] - nums[i]) * maxRight[i + 1])

        return ans