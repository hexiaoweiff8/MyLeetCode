from collections import Counter


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        print(c1.keys())
        print(c2.keys())
        print(sorted(c1.keys()) == sorted(c2.keys()))
        print(Counter(c1.values()))
        print(Counter(c2.values()))
        print(Counter(c1.values()) == Counter(c2.values()))
        return sorted(c1.keys()) == sorted(c2.keys()) and Counter(c1.values()) == Counter(c2.values())


obj = Solution()
print(obj.closeStrings("kyq", "kqy"))
