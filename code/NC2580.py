class Solution(object):
    def countWays(self, ranges):
        """
        :type ranges: List[List[int]]
        :rtype: int
        """
        ranges.sort(key=lambda x: x[0])
        res = 1
        for i in range(1, len(ranges)):
            if ranges[i][0] <= ranges[i-1][1]:
                ranges[i][0] = ranges[i-1][0]
                ranges[i][1] = max(ranges[i][1], ranges[i-1][1])
            else:
                res += 1

        return res