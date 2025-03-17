class Solution(object):
    def minimumSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        zeroIndex = 0
        for index in range(len(s)):
            if s[index] == '0':
                # s = s[:zeroIndex] + "0" + s[zeroIndex: index] + s[index + 1:]
                ans += index - zeroIndex
                zeroIndex += 1
        return ans


obj = Solution()
print(obj.minimumSteps("101"))
print(obj.minimumSteps("100"))
print(obj.minimumSteps("0111"))
print(obj.minimumSteps("11000111"))
print(obj.minimumSteps("001000111"))