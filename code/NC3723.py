class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if num * 9 < sum:
            return ''
        ans = '9' * (sum // 9)
        if sum % 9:
            ans += digits[sum % 9]
        return ans + '0' * (num - len(ans))