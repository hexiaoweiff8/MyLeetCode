class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        dic = {}
        ans = 0
        for i, c in enumerate(word):
            cnt = dic.get(c, 0)
            dic[c] = cnt + 1
            ans += (len(dic) - 1) // 8 + 1

        return ans


obj = Solution()
print(obj.minimumPushes("xycdefghij"))