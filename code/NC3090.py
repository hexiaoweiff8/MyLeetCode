from collections import defaultdict


class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = defaultdict(int)
        l = ans = 0
        for index, c in enumerate(s):
            while dic[c] + 1 > 2:
                dic[s[l]] -= 1
                l += 1
            dic[c] += 1
            ans = max(index - l + 1, ans)
        return ans


obj = Solution()
print(obj.maximumLengthSubstring("bcbbbcba"))
