class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:
                l, r, v = queries[k]
                diff[l] += v
                diff[r + 1] -= v
                if l <= i <= r:
                    sum_d += v
                k += 1
            if sum_d < x:
                return -1
        return k