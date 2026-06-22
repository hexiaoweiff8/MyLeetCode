import collections


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        dic = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        minCount = float("inf")
        counter = collections.Counter(text)
        for key in dic:
            if key not in counter:
                return 0
            minCount = min(minCount, counter[key] // dic[key])

        return minCount