class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = nums[0]
        max_right[n - 1] = nums[n - 1]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], nums[i])
        ans = 0
        for i in range(1, n - 1):
            ans = max(ans, (max_left[i - 1] - nums[i]) * max_right[i + 1])
        return ans