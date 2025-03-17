import heapq


class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        queriesSorted = sorted(enumerate(queries), key=lambda x: x[1])
        intLen = len(intervals)
        ret = [-1] * len(queries)
        stack = []
        index = 0
        for idx, query in queriesSorted:
            while index < intLen and intervals[index][0] <= query:
                heapq.heappush(stack, (intervals[index][1] - intervals[index][0] + 1, intervals[index][1]))
                index += 1
            while stack and stack[0][1] < query:
                heapq.heappop(stack)
            if stack:
                ret[idx] = stack[0][0]
        return ret


obj = Solution()
print(obj.minInterval(intervals=[[1, 4], [2, 4], [3, 6], [4, 4]], queries=[2, 3, 4, 5]))
print(obj.minInterval(intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22]))
print(obj.minInterval(intervals=[[4, 5], [5, 8], [1, 9], [8, 10], [1, 6]], queries=[7, 9, 3, 9, 3]))
