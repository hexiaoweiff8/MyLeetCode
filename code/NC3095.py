class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 999999
        l = r = 0
        val = 0
        while r < len(nums):
            for i in range(l, r):
                val |= nums[i]
            if val >= k:
                ans = min(ans, r - l + 1)



obj = Solution()
print(obj.minimumSubarrayLength([2,1,8], 10))