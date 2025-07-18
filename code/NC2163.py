import heapq
from heapq import heappushpop


class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        n = m // 3
        min_h = nums[-n:]
        heapq.heapify(min_h)

        # 后缀最大和
        suf_max = [0] * (m - n + 1)
        suf_max[-1] = sum(min_h)
        for i in range(m - n - 1, n - 1, -1):
            suf_max[i] = suf_max[i + 1] + nums[i] - heappushpop(min_h, nums[i])

        # 取反构建最大堆
        max_h = [-x for x in nums[:n]]
        heapq.heapify(max_h)

        # 前缀最小和
        pre_min = -sum(max_h)
        # i = n-1时的答案
        ans = pre_min - suf_max[n]
        for i in range(n, m - n):
            pre_min += nums[i] + heappushpop(max_h, -nums[i])
            ans = min(ans, pre_min - suf_max[i + 1])

        return ans

