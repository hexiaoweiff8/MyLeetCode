class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        sum1, sum2 = 0, 0
        sign = 0
        for val in player1:
            sum1 += val
            if sign > 0:
                sum1 += val
                sign = 0 if sign == 2 else (sign + 1)
            if val == 10:
                sign = 1
        sign = 0
        for val in player2:
            sum2 += val
            if sign > 0:
                sum2 += val
                sign = 0 if sign == 2 else (sign + 1)
            if val == 10:
                sign = 1

        return 1 if sum1 > sum2 else (0 if sum1 == sum2 else 2)


obj = Solution()
# print(obj.isWinner([9,7,10], [5,9,0]))
print(obj.isWinner([9,7,10,7], [10,2,4,10]))