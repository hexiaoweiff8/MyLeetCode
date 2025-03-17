class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        ret = count1 = count2 = 0
        for c in text:
            if c == pattern[1]:
                ret += count1
                count2 += 1
            if c == pattern[0]:
                count1 += 1
        return ret + max(count1, count2)