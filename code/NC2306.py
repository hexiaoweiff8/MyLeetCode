class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        dic = set(ideas)
        fWord = [[0] * 26 for _ in range(26)]
        for word in ideas:
            t = list(word)
            for i in range(26):
                t[0] = chr(i + ord('a'))
                if ''.join(t) not in dic:
                    fWord[ord(word[0]) - ord('a')][i] += 1
        ret = 0
        for word in ideas:
            t = list(word)
            for i in range(26):
                t[0] = chr(i + ord('a'))
                if ''.join(t) not in dic:
                    ret += fWord[i][ord(word[0]) - ord('a')]
        return ret