class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        ret = mx = 0
        dp = [0] * len(values)
        for i, v in enumerate(values):
            ret = max(ret, mx + v - i)
            mx = max(mx, v + i)

        return ret
