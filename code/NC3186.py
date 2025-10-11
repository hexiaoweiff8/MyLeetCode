import collections


class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        cnt = collections.Counter(power)
        a = sorted(cnt)
        dp = [0] * (len(a) + 1)
        j = 0
        for i, x in enumerate(a):
            while a[j] < x - 2:
                j += 1
            dp[i + 1] = max(dp[i], dp[j] + x * cnt[x])

        return dp[-1]
