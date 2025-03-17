class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        numLen = len(str(n))
        startSign = 1 if numLen % 2 == 1 else -1
        ret = 0
        while n > 0:
            ret += (n % 10) * startSign
            startSign *= -1
            n //= 10

        return ret


obj = Solution()
print(obj.alternateDigitSum(521))
print(obj.alternateDigitSum(111))
print(obj.alternateDigitSum(886996))