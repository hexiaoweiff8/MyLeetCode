class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        count = 1
        if time[4] == "?":
            count *= 10
        if time[3] == "?":
            count *= 6
        if time[0:2] == "??":
            count *= 24
        elif time[1] == "?":
            if time[0] in ("0", "1"):
                count *= 10
            else:
                count *= 4
        elif time[0] == "?":
            count *= 3 if time[1] in ("0", "1", "2", "3", "?") else 2

        return count

obj = Solution()
print(obj.countTime("?5:00"))
print(obj.countTime("0?:0?"))
print(obj.countTime("??:??"))
print(obj.countTime("07:?3"))
