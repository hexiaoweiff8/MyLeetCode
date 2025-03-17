class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        if 1 < n <= 3:
            return n - 1
        a1, a2, a3, a4 = 1, 1, 2, 4
        for i in range(4, n + 1):
            a4 = a1 + a2 + a3
            a1, a2, a3 = a2, a3, a4
        return a4


obj = Solution()
print(obj.tribonacci(4))