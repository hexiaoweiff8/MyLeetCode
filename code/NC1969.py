class Solution(object):
    def minNonZeroProduct(self, p):
        """
        :type p: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        maxVal = (1 << p) - 1
        return maxVal * pow((maxVal - 1), maxVal >> 1) % MOD


obj = Solution()
print(obj.minNonZeroProduct(22))
