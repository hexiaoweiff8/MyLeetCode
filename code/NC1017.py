class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        if n == 0:
            return "0"
        if n & 1:
            return self.baseNeg2((n - 1) // -2) + "1"
        return self.baseNeg2(n // -2) + "0"


obj = Solution()
print(obj.baseNeg2(2))