import math
from heapq import heapify, heappop, heappush


class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ret = 0
        stack = [-num for num in nums]
        heapify(stack)
        for _ in range(k):
            item = heappop(stack)
            ret += -item
            heappush(stack, -math.ceil(-item / 3))

        return ret


obj = Solution()
print(obj.maxKelements(nums=[10, 10, 10, 10, 10], k=5))
print(obj.maxKelements(nums=[1, 10, 3, 3, 3], k=3))
