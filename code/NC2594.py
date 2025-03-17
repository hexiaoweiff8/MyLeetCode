import math

# 题目具有单调性，可以使用二分查找
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        left, right = 0, min(ranks) * cars * cars
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(math.floor(math.sqrt(mid // r)) for r in ranks) >= cars:
                right = mid
            else:
                left = mid
        return right


obj = Solution()
print(obj.repairCars())