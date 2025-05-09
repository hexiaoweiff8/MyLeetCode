class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        m = len(nums)
        dp = [{} for _ in range(m)]
        for i in range(m):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                ans = max(ans, dp[i][diff])

        return ans