class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        pre = s[0].lower()
        ret = 0
        for i in range(1, len(s)):
            if s[i].lower() != pre:
                ret += 1
                pre = s[i].lower()
        return ret