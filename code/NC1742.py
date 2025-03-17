class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        # 盒子数组
        boxArray = {}
        # 遍历limit
        for ballVal in range(lowLimit, highLimit + 1):
            sum = self.getSum(ballVal)
            boxArray[sum] = 1 + boxArray.get(sum, 0)

        return boxArray[max(boxArray, key=boxArray.get)]

    def getSum(self, val):
        sum = 0
        while val > 0:
            sum += val % 10
            val //= 10

        return sum


obj = Solution()
print(obj.countBalls(1, 28000))

# 超过50%