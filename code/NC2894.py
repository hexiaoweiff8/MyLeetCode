class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1 = 0
        num2 = 0
        for i in range(1, n + 1):
            if i % m == 0:
                num1 += i
            else:
                num2 += i

        return num2 - num1

    def differenceOfSums2(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        return n * (n + 1) // 2 - n // m * (n // m + 1) * m

