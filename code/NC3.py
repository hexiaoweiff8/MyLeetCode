class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len = 1
        start = 0
        end = 1
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
                max_len = max(max_len, end - start)
            else:
                start += 1
        return max_len