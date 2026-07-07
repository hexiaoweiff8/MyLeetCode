class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre = [0] * len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] + nums[i]
        minS = [-9999999] * k
        ans = -9999999
        for j, s in enumerate(pre):
            ans = max(ans, s - minS[j % k])
            minS[j % k] = min(minS[j % k], s)
        return ans