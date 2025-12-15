class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [1] * n
        for i in range(1, n):
            if prices[i] == prices[i - 1] - 1:
                dp[i] = dp[i - 1] + 1

        return sum(dp)