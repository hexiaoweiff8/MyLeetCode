class Solution(object):
    def getSmallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        preC = s[0]
        for i in range(1, len(s)):
            if int(s[i]) % 2 == int(preC) % 2 and int(s[i]) < int(preC):
                return s[:i - 1] + s[i] + preC + s[i + 1:]
            preC = s[i]
        return s


object = Solution()
print(object.getSmallestString("45320"))