class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"Q": 0, "W": 0, "E": 0, "R": 0}
        addDic = {}
        lenS = len(s)
        charCount = lenS // 4

        for char in s:
            dic[char] = dic.get(char, 0) + 1

        # 计算补全的数量
        for key, val in dic.items():
            addDic[key] = charCount - val

        # 补全
        for key, val in addDic.items():
