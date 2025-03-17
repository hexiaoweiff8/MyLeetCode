from collections import defaultdict


class Solution(object):
    def longestEqualSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        posList = defaultdict(list)
        for i, num in enumerate(nums):
            posList[num].append(i)

        res = 0
        for lst in posList.values():
            j = 0
            for i in range(len(lst)):

                while lst[i] - lst[j] - (i - j) > k:
                    j += 1
                res = max(res, i - j + 1)

        return res

