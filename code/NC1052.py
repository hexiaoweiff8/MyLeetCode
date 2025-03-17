class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        if len(customers) == 1:
            return customers[0]
        sumVal = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                sumVal += customers[i]
        for j in range(minutes):
            if j < len(grumpy) and grumpy[j] == 1:
                sumVal += customers[j]
        maxVal = sumVal
        for k in range(minutes, len(customers)):
            if grumpy[k - minutes] == 1:
                sumVal -= customers[k - minutes]
            if grumpy[k] == 1:
                sumVal += customers[k]
            maxVal = max(maxVal, sumVal)

        return maxVal


obj = Solution()
print(obj.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
print(obj.maxSatisfied([1], [0], 1))
print(obj.maxSatisfied([3], [1], 1))
print(obj.maxSatisfied([3, 7], [0, 0], 2))
