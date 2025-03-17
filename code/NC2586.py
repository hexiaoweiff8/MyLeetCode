class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        yuan = ['a', 'e', 'i', 'o', 'u']
        ret = 0
        for index in range(left, right + 1):
            if words[index][0] in yuan and words[index][-1] in yuan:
                ret += 1
        return ret