from heapq import heappop, heappush


class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        n = len(apples)
        ans = 0
        heap = []
        day = 0
        for i in range(n):
            while heap and heap[0][0] <= i:
                heappop(heap)
            if apples[i] > 0:
                heappush(heap, [i + days[i], apples[i]])
            if heap:
                heap[0][1] -= 1
                if heap[0][1] == 0:
                    heappop(heap)
                ans += 1
            day += 1
        while heap:
            while heap and heap[0][0] <= day:
                heappop(heap)
            if heap:
                val = heap[0][1] if heap[0][1] < heap[0][0] - day else heap[0][0] - day
                ans += val
                day += val
                heappop(heap)
        return ans


obj = Solution()
print(obj.eatenApples([1, 2, 3, 5, 2], [3, 2, 1, 4, 2]))
