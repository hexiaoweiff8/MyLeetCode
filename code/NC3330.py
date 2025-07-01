class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 1
        preChar = word[0]
        for i in range(1, len(word)):
            if word[i] == preChar:
                ans += 1
            preChar = word[i]

        return ans