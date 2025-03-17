from itertools import count


class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        # f = [[0] * (k + 1) for _ in range(n + 1)]
        # for i in count(1):
        #     for j in range(k + 1):
        #         f[i][j] = f[i - 1][j] + f[i - 1][j - 1] + 1
        #     if f[i][k] >= n:
        #         return i
        f = [0] * (k + 1)
        for i in count(1):
            for j in range(k, 0, -1):
                f[j] += f[j - 1] + 1
            if f[k] >= n:
                return i