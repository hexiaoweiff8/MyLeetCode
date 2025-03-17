from bisect import bisect_left


class Solution(object):
    def maximizeWin(self, prizePositions, k):
        """
        :type prizePositions: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        n = len(prizePositions)
        f = [0] * (n + 1)
        for i, x in enumerate(prizePositions, 1):
            j = bisect_left(prizePositions, x - k)
            ret = max(ret, i - j + f[j])
            f[i] = max(f[i - 1], i - j)
        return ret