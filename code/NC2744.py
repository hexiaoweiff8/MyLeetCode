class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        seen = set()
        for i, word in enumerate(words):
            if word[::-1] in seen:
                ret += 1
            seen.add(word)
        return ret


obj = Solution()
print(obj.maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
