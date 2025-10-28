class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        ans = pre = 0
        for x in nums:
            if x:
                pre += x
            elif pre * 2 == total:
                ans += 2
            elif abs(pre * 2 - total) == 1:
                ans += 1
        return ans
