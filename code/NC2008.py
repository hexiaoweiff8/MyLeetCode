class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        dp = [0] * (n + 1)
        rideMap = {}
        for ride in rides:
            if ride[1] not in rideMap:
                rideMap[ride[1]] = []
            rideMap[ride[1]].append(ride)
        for i in range(n + 1):
            dp[i] = dp[i - 1]
            if i not in rideMap:
                continue
            for ride in rideMap[i]:
                dp[i] = max(dp[i], dp[ride[0]] + ride[2] - ride[0] + ride[1])
        return dp[n]



