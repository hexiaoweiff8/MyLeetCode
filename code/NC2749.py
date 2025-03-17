from itertools import count


class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        for k in count(1):
            x = num1 - num2 * k
            if x < k:
                return - 1
            if k >= x.bit_count():
                return k
