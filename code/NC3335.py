class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        for round in range(t):
            new_cnt = [0] * 26
            new_cnt[0] = cnt[25]
            new_cnt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                new_cnt[i] = cnt[i - 1]
            cnt = new_cnt
        return sum(cnt) % mod