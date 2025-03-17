class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        n = len(nextVisit)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % mod
        return (dp[-1] - 1) % mod


