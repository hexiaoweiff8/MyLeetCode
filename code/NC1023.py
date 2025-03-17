import re


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        ret = []



        return ret
        # def fullmatch(regex, string, flags=0):
        #     """Emulate python-3.4 re.fullmatch()."""
        #     return re.match("(?:" + regex + r")\Z", string, flags=flags)
        # # pattern改成正则
        # newPattern = r"[a-z]*"
        # ret = []
        # for char in pattern:
        #     newPattern += char + r"[a-z]*"
        #
        # for query in queries:
        #     ret.append(True if fullmatch(newPattern, query) else False)
        #
        # return ret


obj = Solution()
print(obj.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"))
#
# regex2 = re.compile("[a-z]*P[a-z]*B[a-z]*")
# print(regex2.fullmatch("FooBar"))
# print(regex2.fullmatch("FooBarTest"))
# print(regex2.fullmatch("FootBall"))
# print(regex2.fullmatch("FrameBuffer"))
# print(regex2.fullmatch("ForceFeedBack"))
