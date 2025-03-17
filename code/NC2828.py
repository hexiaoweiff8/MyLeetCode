class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        if len(s) != len(words):
            return False
        for i in range(len(s)):
            if s[i] != words[i][0]:
                return False
        return True


