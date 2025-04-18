class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(n):
                if nums[j] <= i:
                    dp[i] += dp[i - nums[j]]
        return dp[-1]