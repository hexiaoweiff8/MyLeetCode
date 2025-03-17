from collections import Counter


class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        wordsCounter1 = Counter(words1)
        wordsCounter2 = Counter(words2)
        return sum(1 for word in wordsCounter1 if wordsCounter1[word] == 1 and wordsCounter2[word] == 1)