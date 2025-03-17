class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = 0
        tmp = x
        while x:
            s += x % 10
            x //= 10

        return s if tmp % s == 0 else -1