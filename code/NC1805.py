class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        # 循环处理字符, 如果碰到数字则将数字拼入子串, 如果碰到非数字则将子串放入字典并计数
        lenCount = len(word)
        subStr = ''
        digitCount = 0
        digitDict = {}
        for index in range(lenCount):
            char = word[index]
            if char.isdigit():
                # 如果是数字则 拼入子串
                subStr += char
            elif len(subStr) > 0:
                # 如果非数字则将子串放入字典并计数
                if digitDict.get(int(subStr), None) is None:
                    digitDict[int(subStr)] = 1
                    digitCount += 1
                subStr = ''
        if len(subStr) > 0:
            if digitDict.get(int(subStr), None) is None:
                digitDict[int(subStr)] = 1
                digitCount += 1
        return digitCount

obj = Solution()
print(obj.numDifferentIntegers('a1b01c001'))
