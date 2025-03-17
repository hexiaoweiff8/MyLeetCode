class Solution(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        n = len(nums)
        f = nums[:]
        ret = sum(f)
        for k in range(1, n):
            for i in range(n):
                f[i] = min(f[i], nums[(i + k) % n])
            ret = min(ret, k * x + sum(f))
        return ret