class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        max_right = 0
        for _, right in intervals:
            if right > max_right:
                ans += 1
                max_right = right

        return ans

obj = Solution()
print(obj.removeCoveredIntervals([[1,2],[1,4],[3,4]]))