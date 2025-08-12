class Solution(object):
    def numberOfWays(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        f = [1] + [0] * n
        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break
            for s in range(n, v - 1, -1):
                f[s] += f[s - v]
        return f[n] % (10 ** 9 + 7)