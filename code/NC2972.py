class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = 0
        l = 1
        while l < n and nums[l - 1] < nums[l]:
            l += 1
        ret += l + (l < n)
        for r in range(n - 2, -1, -1):
            while l > 0 and nums[l - 1] >= nums[r + 1]:
                l -= 1
            ret += l + (l <= r)
            if nums[r] >= nums[r + 1]:
                break
        return ret


