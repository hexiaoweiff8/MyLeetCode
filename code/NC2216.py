class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, n = 0, len(nums)
        for i in range(n):
            if (i - ret) % 2 == 0 and i + 1 < n and nums[i] == nums[i + 1]:
                ret += 1
        return ret + 1 if (n - ret) % 2 != 0 else ret