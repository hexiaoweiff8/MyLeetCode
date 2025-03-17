class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ret, left = 0, 0
        cnt = [0, 0]
        for right, ch in enumerate(s):
            cnt[ch == '0'] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[s[left] == '0'] -= 1
                left += 1
            ret += right - left + 1
        return ret