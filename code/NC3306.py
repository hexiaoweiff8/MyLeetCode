class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        yuanChar = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        def count(m):
            n, res, cons = len(word), 0, 0
            occ = {}
            j = 0
            for i in range(n):
                while j < n and (cons < m or len(occ) < 5):
                    if word[j] in yuanChar:
                        occ[word[j]] = occ.get(word[j], 0) + 1
                    else:
                        cons += 1
                    j += 1
                if len(occ) == 5 and cons >= m:
                    res += n - j + 1
                if word[i] in yuanChar:
                    occ[word[i]] -= 1
                    if occ[word[i]] == 0:
                        del occ[word[i]]
                else:
                    cons -= 1
            return res

        return count(k) - count(k + 1)