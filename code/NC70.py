class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, q, r = 0, 0, 1
        for i in range(n):
            p, q = q, r
            r = p + q
        return r




