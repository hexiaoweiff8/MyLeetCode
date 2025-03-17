class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        index1, index2 = 0, len(s) - 1
        charList = list(s)
        while index1 < index2:
            if charList[index1] != charList[index2]:
                if charList[index1] < charList[index2]:
                    charList[index2] = charList[index1]
                else:
                    charList[index1] = charList[index2]
            index1 += 1
            index2 -= 1
        return "".join(charList)


obj = Solution()
print(obj.makeSmallestPalindrome("egcfe"))
print(obj.makeSmallestPalindrome("abcd"))
print(obj.makeSmallestPalindrome("seven"))