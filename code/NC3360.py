class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = 10
        while n >= t:
            n -= t
            t -= 1
        return t % 2 == 1

obj = Solution()
print(obj.canAliceWin(19))
