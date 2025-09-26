from bisect import bisect_left


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans += bisect_left(nums, nums[i] + nums[j], j + 1, n) - j - 1

        return ans