from numpy import gcd


class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(nums[i], nums[j]):
                    res += 1
        return res