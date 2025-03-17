class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        i, j, refill = 0, len(plants) - 1, 0
        a, b = capacityA, capacityB
        if i == j:
            return 0
        while i < j:
            if a < plants[i]:
                a = capacityA
                refill += 1
            a -= plants[i]
            i += 1
            if b < plants[j]:
                b = capacityB
                refill += 1
            b -= plants[j]
            j -= 1
        return refill + (1 if i == j and a < plants[i] and b < plants[i] else 0)


obj = Solution()
# print(obj.minimumRefill([2, 2, 3, 3], 5, 5))
# print(obj.minimumRefill([5], 10, 8))
# print(obj.minimumRefill([1, 2, 4, 4, 5], 6, 5))
print(obj.minimumRefill([2, 1, 1], 2, 2))
