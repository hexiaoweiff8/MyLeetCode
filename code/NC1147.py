class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        ret = 0
        lastIndexEnd = lastIndexStart = len(text)
        half = len(text) // 2
        index = 0
        while index <= half and 0 <= lastIndexStart:
            char = text[index]
            lastIndex = text.rfind(char, 0, lastIndexStart)
            # print(index, lastIndex)
            # print(text[index: index + lastIndexEnd - lastIndex], text[lastIndex: lastIndexEnd])
            if 0 <= lastIndex != index and half <= lastIndex \
                    and text[index: index + lastIndexEnd - lastIndex] == text[lastIndex: lastIndexEnd]:
                ret += 2
                index += lastIndexEnd - lastIndex
                lastIndexEnd = lastIndex
            elif index == lastIndex:
                ret += 1
            lastIndexStart = lastIndex

        return ret


obj = Solution()
print(obj.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
print(obj.longestDecomposition("merchant"))
print(obj.longestDecomposition("antaprezatepzapreanta"))
print(obj.longestDecomposition("aaa"))
print(obj.longestDecomposition("elvtoelvto"))
print(obj.longestDecomposition("fkhsotfvbp"))
print(obj.longestDecomposition("vwsuvmbwknmnvwsuvmbwk"))
print(obj.longestDecomposition("rrstkbncgfdvtszniury"))