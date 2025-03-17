import heapq


class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        stack = []
        for num in nums:
            heapq.heappush(stack, num)
        while stack[0] < k and len(stack) > 1:
            x = heapq.heappop(stack)
            y = heapq.heappop(stack)
            heapq.heappush(stack, min(x, y) * 2 + max(x, y))
            ans += 1
        return ans


obj = Solution()
print(obj.minOperations([2, 11, 10, 1, 3], 10))
