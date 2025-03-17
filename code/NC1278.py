class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = self.min_change(s[:i + 1])
        for j in range(2, k + 1):
            for i in range(j - 1, n):
                dp[i][j] = min([dp[m][j - 1] + self.min_change(s[m + 1:i + 1])
                                for m in range(j - 2, i)])
        return dp[-1][-1]

    def min_change(self, s):
        l = 0
        r = len(s) - 1
        res = 0
        while l < r:
            if s[l] != s[r]:
                res += 1
            l += 1
            r -= 1
        return res