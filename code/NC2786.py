class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        dp = [[0] * (x + 1) for _ in range(2)]
        for i in range(n):
            dp[i % 2][0] = max(dp[(i - 1) % 2][0], dp[(i - 1) % 2][-1])
            dp[i % 2][x] = max(dp[(i - 1) % 2][x], dp[(i - 1) % 2][x - 1])
            for j in range(1, x):
                dp[i % 2][j] = max(dp[(i - 1) % 2][j - 1], nums[i] + dp[(i - 1) % 2][j - 1], nums[i] + dp[(i - 1) % 2][j])
        return max(dp[n % 2][:x])