from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(sqrt(c))
        while l <= r:
            if l * l + r * r < c:
                l += 1
            elif l * l + r * r > c:
                r -= 1
            else:
                return True
        return False