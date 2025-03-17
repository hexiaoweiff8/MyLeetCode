class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 循环所有字符,
        strLen = len(s)
        preChar = ''
        count = 0
        stageCount = 0
        for index in range(strLen):
            char = s[index]
            stageCount = stageCount + 1 if char == preChar else 1
            count += stageCount
            preChar = char

        return count % 1000000007


obj = Solution()
print(obj.countHomogenous('zzzzz'))
