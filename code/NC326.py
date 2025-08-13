class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 2:
            return False
        while n > 1:
            n //= 3
        return n == 1


obj = Solution()
print(obj.isPowerOfThree(45))
