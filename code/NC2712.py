class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # ans = 0
        # for i in range(n - 1):
        #     if s[i] != s[i + 1]:
        #         ans += min(i + 1, n - i - 1)
        # return ans
        dp = [0] * n
        for i in range(n // 2):
            if s[i] == s[i + 1]:
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = dp[i] + 1 + i
        for i in range(n // 2 + 1, n):
            if s[i] == s[i - 1]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + 1 + (i - 1)
        return dp[-1]