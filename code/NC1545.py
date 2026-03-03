class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def invert(s):
            return ''.join('1' if c == '0' else '0' for c in s)
        def reverse(s):
            return s[::-1]
        tmpS = "0"
        while n > 1:
            tmpS = tmpS + "1" + reverse(invert(tmpS))
            n -= 1
        return tmpS[k - 1]
