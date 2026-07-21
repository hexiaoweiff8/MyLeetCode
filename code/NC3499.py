class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = mx = cnt = 0
        pre = -float('inf')
        for i, c in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or c != s[i + 1]:
                if c == '1':
                    total += cnt
                else:
                    mx = max(mx, pre + cnt)
                    pre = cnt
                cnt = 0
        return total + mx