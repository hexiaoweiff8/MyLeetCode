class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        wN = len(word)
        ret = ord(word[0]) - ord(word[wN - 1]) + 2
        for i in range(1, wN):
            ret += (ord(word[i]) - ord(word[i - 1]) + 2) % 3
        return ret


obj = Solution()
# print(obj.addMinimum("b"))
# print(obj.addMinimum("aaa"))
# print(obj.addMinimum("abc"))
print(obj.addMinimum("aaaaab"))
