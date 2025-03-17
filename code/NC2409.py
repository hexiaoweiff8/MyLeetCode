class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ret = 0
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        count1 = sum(days[:int(start[:2]) - 1]) + int(start[3:])
        count2 = sum(days[:int(end[:2]) - 1]) + int(end[3:])
        return max(count2 - count1 + 1, 0)


obj = Solution()
# print(obj.countDaysTogether("09-01",
#                             "10-19",
#                             "06-19",
#                             "10-20"))
# print(obj.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
print(obj.countDaysTogether("03-05",
                            "07-14",
                            "04-14",
                            "09-21"))
print(obj.countDaysTogether("04-20",
                            "06-18",
                            "04-12",
                            "12-19"))
