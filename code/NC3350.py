class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = pre_cnt = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == n - 1 or x >= nums[i + 1]:
                ans = max(ans, cnt // 2, min(cnt, pre_cnt))
                pre_cnt = cnt
                cnt = 0

        return ans
