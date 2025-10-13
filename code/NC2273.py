class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i-1]):
                res.append(words[i])
        return res

