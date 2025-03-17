class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)
        startIndex = 0
        endIndex = strLen - 1
        isDiffient = False
        if startIndex == endIndex:
            return 1
        while startIndex < endIndex:
            isDiffient = True
            startChar = s[startIndex]
            endChar = s[endIndex]
            if startChar == endChar:
                isDiffient = False
                isPlus = False
                if s[startIndex + 1] == startChar:
                    startIndex += 1
                    isPlus = True
                if s[endIndex - 1] == endChar and endIndex > startIndex:
                    endIndex -= 1
                    isPlus = True
                if not isPlus:
                    # 下一个位置如果相同则继续, 不同则返回
                    if startIndex + 1 != endIndex - 1:
                        startIndex += 1
                        endIndex -= 1
                        nextStartChar = s[startIndex]
                        nextEndChar = s[endIndex]
                        if nextStartChar != nextEndChar:
                            isDiffient = True
                            break
                    else:
                        isDiffient = True
                        startIndex += 1
                        endIndex -= 1
                        break
            else:
                break
        return endIndex - startIndex + (1 if isDiffient else 0)


obj = Solution()
print(obj.minimumLength("ca"))
# abbbbbbbbbbbbbbbbbbba 0
# bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb 1

'''
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while right >= left and s[right] == c:
                right -= 1
        return right - left + 1

'''