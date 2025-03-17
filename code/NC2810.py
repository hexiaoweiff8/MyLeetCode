class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        isTail = True
        for c in s:
            if c == 'i':
                isTail = not isTail
            else:
                if isTail:
                    ret.append(c)
                else:
                    ret.insert(0, c)
        return ''.join(ret if isTail else reversed(ret))


obj = Solution()
print(obj.finalString("string"))