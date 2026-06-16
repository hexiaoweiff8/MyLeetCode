class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)):
            if s[i] == "*":
                if result:
                    result.pop()
            elif s[i] == "#":
                if result:
                    result += result
            elif s[i] == "%":
                result.reverse()
            else:
                result.append(s[i])
        return "".join(result)
