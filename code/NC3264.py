import heapq


class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        # 创建小端堆, 元素是(num, index) 按照num排序
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        while k > 0:
            num, index = heapq.heappop(heap)
            nums[index] = num * multiplier
            heapq.heappush(heap, (nums[index], index))
            k -= 1
        return nums