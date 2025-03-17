from itertools import accumulate


class Solution(object):
    def maxValueOfCoins(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        f = [[0] * (k + 1) for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            for j in range(k + 1):
                f[i + 1][j] = f[i][j]
                for w, v in enumerate(accumulate(nums[:j]), 1):
                    f[i + 1][j] = max(f[i + 1][j], f[i][j - w] + v)
        return f[-1][k]