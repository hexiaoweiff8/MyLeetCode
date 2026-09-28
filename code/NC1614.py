class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        dep = ans = 0
        for c in s:
            if c == '(':
                dep += 1
                ans = max(ans, dep)
            elif c == ')':
                dep -= 1
        return ans