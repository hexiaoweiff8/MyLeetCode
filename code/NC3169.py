
class Solution(object):
    def countDays(self, days, meetings):
        """
        :type days: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        n = len(meetings)
        meetings.sort(key=lambda x: x[0])
        start, end = 1, 0
        for s, e in meetings:
            if s > end:
                days -= end - start + 1
                start = s
            end = max(end, e)
        days -= end - start + 1
        return days


obj = Solution()
print(obj.countDays(8, [[3, 4], [4, 8], [2, 5], [3, 8]]))
