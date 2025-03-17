class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        m = len(key)
        dp = [[float('inf')] * m for _ in range(n)]
        for i in range(n):
            if ring[i] == key[0]:
                dp[i][0] = min(i, n - i)
        for j in range(1, m):
            for i in range(n):
                for k in range(n):
                    if ring[k] == key[j]:
                        dp[k][j] = min(dp[k][j], dp[i][j - 1] + min(abs(k - i), n - abs(k - i)))
        return min(dp[i][m - 1] for i in range(n)) + m
