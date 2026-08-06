class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        ans = -1
        while ans < 0:
            index = n
            numVal = 1
            while index > 0:
                numVal *= index % 10
                index //= 10
            if numVal % t == 0:
                ans = n
            else:
                n += 1
        return ans