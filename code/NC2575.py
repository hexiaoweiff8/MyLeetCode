class Solution(object):
    def divisibilityArray(self, word, m):
        """
        :type word: str
        :type m: int
        :rtype: List[int]
        """
        res = []
        num = 0
        for index in range(len(word)):
            num = (num * 10 + int(word[index])) % m
            res.append(1 if num == 0 else 0)
        return res