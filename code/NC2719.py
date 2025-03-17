class Solution(object):
    def count(self, num1, num2, min_sum, max_sum):
        """
        :type num1: str
        :type num2: str
        :type min_sum: int
        :type max_sum: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        maxCount = int(num2) - int(num1)
        # 计算单个进位内超过数值的数量关系