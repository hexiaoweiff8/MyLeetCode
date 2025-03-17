class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = s.split(" ")
        preNum = -1
        isGroup = True
        for item in strs:
            if item.isdigit():
                if preNum < int(item):
                    preNum = int(item)
                else:
                    isGroup = False
                    break

        return isGroup

obj = Solution()
print(obj.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
