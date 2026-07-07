from math import sqrt


class Solution(object):
    def xorAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        limit = int(sqrt(n))
        diff = {}
        for l, r, k, v in queries:
            if k > limit:
                for i in range(l, r + 1, k):
                    nums[i] *= v
                    nums[i] %= MOD
                continue

            m = l % k
            key = (k, m)
            if key not in diff:
                diff[key] = [1] * (n + 2)

            diff[key][(l - m) // k] *= pow(v, MOD - 2, MOD)
