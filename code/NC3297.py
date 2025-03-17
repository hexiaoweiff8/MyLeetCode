from collections import Counter


class Solution(object):
    def validSubstringCount(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if len(word1) < len(word2):
            return 0
        cnt = Counter(word2)
        need = len(cnt)
        ans = l = 0
        win = Counter()
        for c in word1:
            win[c] += 1
            if win[c] == cnt[c]:
                need -= 1
            while need == 0:
                if win[word1[l]] == cnt[word1[l]]:
                    need += 1
                win[word1[l]] -= 1
                l += 1
            ans += l
        return ans