from bisect import bisect_left


class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        ans = 999999999
        while p:
            for num in nums:
                i = bisect_left(nums, num - ans)
                if i < len(nums):
                    ans = min(ans, nums[i] - num)
                if i < len(nums) - 1:
                    ans = min(ans, nums[i + 1] - num)
            p -= 1

        return ans