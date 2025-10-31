import collections


class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = collections.Counter(nums)
        res = []
        for k, v in cnt.items():
            if v == 2:
                res.append(k)
        return res
