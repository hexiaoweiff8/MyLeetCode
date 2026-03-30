import collections


class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 先对s1 s2的在奇数位置和偶数位置上的每种字母数量进行统计.
        s1_odd = collections.Counter(s1[1::2])
        s1_even = collections.Counter(s1[::2])
        s2_odd = collections.Counter(s2[1::2])
        s2_even = collections.Counter(s2[::2])
        # 如果不相同则返回false
        if s1_odd != s2_odd or s1_even != s2_even:
            return False
        return True