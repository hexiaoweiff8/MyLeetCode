class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = i = l = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                l += 1
                i += 1
                continue
            if l > 0:
                l -= 1
            else:
                ans += 1

            if i < n - 1 and s[i + 1] == ')':
                i += 2
            else:
                ans += 1
                i += 1
        return ans + l * 2

obj = Solution()
# print(obj.minInsertions("))())("))
print(obj.minInsertions(")))))))"))
