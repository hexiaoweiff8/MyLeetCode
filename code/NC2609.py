class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxCount, zeroCount, oneCount = 0, 0, 0
        for char in s:
            if char == '0':
                if oneCount > 0:
                    maxCount = max(maxCount, min(zeroCount, oneCount))
                    zeroCount = 0
                zeroCount += 1
                oneCount = 0
            else:
                oneCount += 1
        maxCount = max(maxCount, min(zeroCount, oneCount))
        return maxCount * 2


obj = Solution()
print(obj.findTheLongestBalancedSubstring("01000111"))