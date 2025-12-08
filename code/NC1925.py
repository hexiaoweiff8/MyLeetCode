import math


class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        n2 = n * n
        for a in range(1, n):
            a2 = a * a
            for b in range(1, a):
                if a2 + b * b > n2:
                    break
                c2 = a2 + b * b
                if int(math.sqrt(c2)) ** 2 == c2:
                    ans += 2

        return ans
