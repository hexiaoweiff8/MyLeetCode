from collections import Counter


class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        ans = []
        stk = []
        mi = 'a'
        for c in s:
            cnt[c] -= 1
            while mi < 'z' and cnt[mi] == 0:
                mi = chr(ord(mi) + 1)
            stk.append(c)
            while stk and stk[-1] <= mi:
                ans.append(stk.pop())
        return ''.join(ans)



obj = Solution()
print(obj.robotWithString("bdda"))