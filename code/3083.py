from itertools import pairwise


class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # dic = {}
        # for index in range(len(s) - 1):
        #     dic[s[index:index + 2]] = 1
        # # 翻转字符串
        # s = s[::-1]
        # for index in range(len(s) - 1):
        #     if s[index:index + 2] in dic:
        #         return True
        # return False
        vis = set()
        for x, y in pairwise(s):
            vis.add((x, y))
            if (y, x) in vis:
                return True
        return False