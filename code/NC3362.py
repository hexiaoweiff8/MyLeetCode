import heapq


class Solution(object):
    def maxRemoval(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        queries.sort(key=lambda x: x[0])
        h = []
        diff = [0] * (len(nums) + 1)
        sumD = j = 0
        for i, x in enumerate(nums):
            sumD += diff[i]
            while j < len(queries) and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1
            while sumD < x and h and -h[0] >= i:
                sumD += 1
                diff[-heapq.heappop(h) + 1] -= 1
            if sumD < x:
                return -1
        return len(h)