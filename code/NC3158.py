from collections import Counter


class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        ret = 0
        for k, v in counter.items():
            if v > 1:
                ret ^= k
        return ret