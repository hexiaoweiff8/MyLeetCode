import math


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        # 循环n次, 减去与index相同的rollmax值
        result = math.pow(6, n)
        for index in range(n):


        return result % 1000000007