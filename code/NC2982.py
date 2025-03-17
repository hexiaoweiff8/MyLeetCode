class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == s[dp[i - 1]]:
                dp[i] = dp[i - 1] + 1
        return max(dp)