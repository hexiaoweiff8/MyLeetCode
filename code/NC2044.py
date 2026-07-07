class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = max(nums)
        cnt = 0
        for num in nums:
            if num == max_or:
                cnt += 1
