class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ct1, ct2 = 1, 1
        ans = 1
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                ans = max(ans, ct1)
                ct1 = 1
            else:
                ct1 += 1
            if nums[i] >= nums[i - 1]:
                ans = max(ans, ct2)
                ct2 = 1
            else:
                ct2 += 1
        ans = max(ans, max(ct1, ct2))
        return ans


obj = Solution()
print(obj.longestMonotonicSubarray([1,4,3,3,2]))
