class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        allCharMapList = []
        ret = 0
        for word in words:
            charMap = set(word)
            allCharMapList.append([word, charMap])

        for index, array in enumerate(allCharMapList):
            for index2 in range(index + 1, len(allCharMapList)):
                if array[1].intersection(allCharMapList[index2][1]):
                    continue
                else:
                    ret = max(len(array[0]) * len(allCharMapList[index2][0]), ret)
        return ret


obj = Solution()
# print(obj.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(obj.maxProduct(["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]))
