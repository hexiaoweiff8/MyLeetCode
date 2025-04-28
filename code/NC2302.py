class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        ans = 0
        l, r = 1, 1
        while r < n + 1:
            while r < n + 1 and (preSum[r] - preSum[l - 1]) * (r - l + 1) < k:
                r += 1
                ans += r - l
            l += 1

        return ans


obj = Solution()
print(obj.countSubarrays([2, 1, 4, 3, 5], 10))
