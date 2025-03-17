class Solution(object):
    def checkPartitioning(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if (j == i or j == i + 1 or dp[i + 1][j - 1]) and s[i] == s[j]:
                    dp[i][j] = True
        for i in range(2, n):
            for j in range(i - 1):
                if dp[0][j] and dp[j + 1][i - 1] and dp[i][-1]:
                    return True
        return False