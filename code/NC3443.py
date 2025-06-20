class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 统计横向/纵向距离
        h, v = 0, 0
        ans = 0
        for i in range(len(s)):
            if s[i] == 'N':
                h += 1
            elif s[i] == 'S':
                h -= 1
            elif s[i] == 'E':
                v += 1
            elif s[i] == 'W':
                v -= 1
            ans = max(ans, min(i + 1, abs(v) + abs(h) + k * 2))
        return ans


obj = Solution()
print(obj.maxDistance(s="NWSE", k=1))
