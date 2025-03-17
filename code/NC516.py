class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # for i in range(n - 1, -1, -1):
        #     dp[i][i] = 1
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i + 1][j - 1] + 2
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # return dp[0][n - 1]

        # def dfs(i, j):
        #     if i > j:
        #         return 0
        #     if dp[i][j] != 0:
        #         return dp[i][j]
        #     if s[i] == s[j]:
        #         dp[i][j] = dfs(i + 1, j - 1) + 2
        #     else:
        #         dp[i][j] = max(dfs(i + 1, j), dfs(i, j - 1))
        #     return dp[i][j]
        # return dfs(0, n - 1)
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]