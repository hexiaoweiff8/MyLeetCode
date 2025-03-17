class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for i in range(target+1)] for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(1,target+1):
                for l in range(1,k+1):
                    if j-l >= 0:
                        dp[i][j] += dp[i-1][j-l]
                        dp[i][j] %= 1000000007

        return dp[n][target]