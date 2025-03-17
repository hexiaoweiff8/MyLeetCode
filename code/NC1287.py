import collections

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = collections.Counter(arr)
        allCount = len(arr)
        for key, value in counter.items():
            if value > allCount / 4:
                return key
