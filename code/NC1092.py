class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # 获取字符串相似部分, 如果没有则拼接两个字符串
        str1Len = len(str1)
        str2Len = len(str2)
        if str1 == str2:
            return str1
        elif str1Len < str2Len:
            tmpStr = str2
            str2 = str1
            str1 = tmpStr
        # 判断1的内部有没有2
        if str2 in str1:
            return str1
        # 判断1的结尾又没有部分2
        index1 = self.isEndPard(str1, str2)
        # 判断2的结尾又没有部分1
        index2 = self.isEndPard(str2, str1)
        if index1 > index2:
            return str1 + str2[index1:]
        elif index1 < index2:
            return str2 + str1[index2:]
        elif index1 > 0:
            return str1 + str2[index1:]
        return str1 + str2

    def isEndPard(self, strFrom, strTo):
        # 二分法查找结尾子串
        lenTo = len(strTo)
        halfLen = lenTo // 2
        plus = halfLen
        lastEndIndex = -1
        while True:
            if strTo[: halfLen] in strFrom:
                lastEndIndex = halfLen
                plus //= 2
                if plus == 0:
                    break
                halfLen += plus
            else:
                plus //= 2
                if plus == 0:
                    break
                halfLen -= plus
        if strFrom.endswith(strTo[: lastEndIndex]):
            return lastEndIndex
        else:
            return -1


obj = Solution()
print(obj.shortestCommonSupersequence("abac", "cab"))
print(obj.shortestCommonSupersequence("123456", "456"))
print(obj.shortestCommonSupersequence("456", "123456"))
print(obj.shortestCommonSupersequence("12345", "234"))
print(obj.shortestCommonSupersequence("1234", "112451"))
print(obj.shortestCommonSupersequence("bbbaaaba", "bbababbb"))
"bbabaaababb"
"bbababbbaaaba"