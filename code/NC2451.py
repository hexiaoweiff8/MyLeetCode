class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dic = {"a": 0,
               "b": 1,
               "c": 2,
               "d": 3,
               "e": 4,
               "f": 5,
               "g": 6,
               "h": 7,
               "i": 8,
               "j": 9,
               "k": 10,
               "l": 11,
               "m": 12,
               "n": 13,
               "o": 14,
               "p": 15,
               "q": 16,
               "r": 17,
               "s": 18,
               "t": 19,
               "u": 20,
               "v": 21,
               "w": 22,
               "x": 23,
               "y": 24,
               "z": 25}
        extrWord = ""
        extrWord2 = ""
        preEq = False
        preValueArray = []
        count = 0
        for word in words:
            valueArray = []
            for index in range(1, len(word)):
                valueArray.append(dic[word[index]] - dic[word[index - 1]])
            if preValueArray != valueArray:
                if count > 1:
                    if preEq:
                        return word
                    else:
                        return extrWord
                elif preEq:
                    return extrWord
                else:
                    extrWord2 = extrWord
                    extrWord = word
                preEq = False
            else:
                preEq = True
                if extrWord2:
                    return extrWord2
            count += 1
            preValueArray = valueArray


obj = Solution()
print(obj.oddString(["adc","wzy","abc"]))
print(obj.oddString(["aaa","bob","ccc","ddd"]))
print(obj.oddString(["bob","aaa","ccc","ddd"]))
