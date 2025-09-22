import collections


class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        ans = 0
        maxCount = max(counts.values())
        for val, count in counts.items():
            if count == maxCount:
                ans += count

        return ans