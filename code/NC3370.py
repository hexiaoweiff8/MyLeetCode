class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        sourceN = n
        bitVal = 0
        while n > 0:
            bitVal += 1
            bitVal <<= 1
            n //= 2

        if sourceN < bitVal:
            return bitVal // 2
        return bitVal - 1


obj = Solution()
print(obj.smallestNumber(5))