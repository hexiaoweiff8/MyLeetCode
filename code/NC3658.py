class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        return gcd(sum([2 * i for i in range(1, n + 1)]), sum([2 * i - 1 for i in range(1, n + 1)]))