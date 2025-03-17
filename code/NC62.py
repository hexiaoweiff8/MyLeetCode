class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for index1 in range(1, m):
            for index2 in range(1, n):
                dp[index1][index2] = dp[index1 - 1][index2] + dp[index1][index2 - 1]

        return dp[-1][-1]
