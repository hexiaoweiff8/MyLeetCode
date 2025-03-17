class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n if n % 2 == 0 else 2 * n


obj = Solution()
print(obj.smallestEvenMultiple(5))
print(obj.smallestEvenMultiple(6))