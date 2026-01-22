from itertools import pairwise


class Solution(object):
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        while any(x > y for x, y in pairwise(nums)):
            cand = 0
            mn = float('inf')
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] < mn:
                    cand = i
                    mn = nums[i] + nums[i + 1]
            nums = nums[:cand] + [mn] + nums[cand + 2:]
            ans += 1

        return ans

