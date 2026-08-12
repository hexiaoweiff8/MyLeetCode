from collections import defaultdict


class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = defaultdict(int)
        maxVal = 0
        l, r = 0, 0
        while r < len(nums):
            dic[nums[r]] += 1
            while dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l += 1
            r += 1
            maxVal = max(maxVal, r - l)

        return maxVal


obj = Solution()
print(obj.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
