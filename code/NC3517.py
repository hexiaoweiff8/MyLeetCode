
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = len(s) // 2
        base = sorted(s[:p])
        mid = [s[p]] if len(s) % 2 == 1 else []
        reversed_base = base[::-1]
        return "".join(base + mid + reversed_base)

