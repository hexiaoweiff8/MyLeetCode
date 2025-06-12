class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums.append(nums[0])
        for i in range(len(nums) - 1):
            ans = max(ans, abs(nums[i] - nums[i + 1]))
        return ans