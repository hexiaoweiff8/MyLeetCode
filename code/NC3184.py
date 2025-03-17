from collections import Counter


class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        ret = Counter()
        dic = {}
        for x in hours:
            ret += dic[(24 - (x % 24)) % 24]
            dic[x % 24] += 1