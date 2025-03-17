class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        m = len(cuts)
        cuts.sort()
        dp = [[0] * (m + 2) for _ in range(m + 2)]
        for i in range(m + 2):
            dp[i][i] = 0
            for j in range(i + 2, m + 2):
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (cuts[j] - cuts[i]) * (cuts[k] - cuts[i]) * (n - cuts[j] + cuts[i]))
                    print(dp)

        return dp[0][m + 1]
