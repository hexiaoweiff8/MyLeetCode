class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(26):
            left = s.find(chr(ord('a') + i))
            if left == -1:
                continue
            right = s.rfind(chr(ord('a') + i))
            ans += len(set(s[left + 1:right]))

        return ans