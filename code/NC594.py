from collections import Counter


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        ans = 0
        for i in nums:
            if count[i] and count[i + 1]:
                ans = max(ans, count[i] + count[i + 1])
            if count[i] and count[i - 1]:
                ans = max(ans, count[i] + count[i - 1])
        return ans