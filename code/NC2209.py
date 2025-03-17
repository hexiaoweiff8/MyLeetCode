from itertools import accumulate


class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        floor = list(map(int,floor))
        n = len(floor)
        dp = [[0]*(n+1) for _ in range(numCarpets+1)]
        dp[0] = list(accumulate(floor))
        for i in range(1,numCarpets+1):
            for j in range(carpetLen * i, n):
                dp[i][j] = min(dp[i][j - 1] + floor[j], dp[i - 1][j - carpetLen])
        return dp[-1][-1]