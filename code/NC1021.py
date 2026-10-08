class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        deep = 0
        for c in s:
            if c == '(':
                deep += 1
                if deep > 1:
                    ans += c
            elif c == ')':
                deep -= 1
                if deep > 0:
                    ans += c
        return ans
