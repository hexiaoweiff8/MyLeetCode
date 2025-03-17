class Solution(object):
    def smallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = list(s)
        for i in range(n):
            if s[i].islower():
                ret[i] = 'a'
            else:
                ret[i] = 'A'
        return ''.join(ret)