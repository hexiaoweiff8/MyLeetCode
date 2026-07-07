class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        sumVal = 0
        for num in str(n):
            if num != '0':
                ans += int(num)
                ans *= 10
                sumVal += int(num)

        return ans // 10 * sumVal