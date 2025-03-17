class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        for c in s:
            if c == '[':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    res += 1
        return (res + 1) // 2
