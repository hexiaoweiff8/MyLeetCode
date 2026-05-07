from itertools import accumulate


class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre_max = list(accumulate(nums, max))

        ans = [0] * n
        suf_min = float('inf')
        for i in range(n - 1, -1, -1):
            ans[i] = pre_max[i] if pre_max[i] <= suf_min else ans[i + 1]
            suf_min = min(nums[i], suf_min)
        return ans