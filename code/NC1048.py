class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        # 从短到长排序
        words.sort(key=len)
        cnt = {}
        for word in words:
            cnt[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                if prev in cnt:
                    cnt[word] = max(cnt[word], cnt[prev] + 1)
            ret = max(ret, cnt[word])
        return ret


obj = Solution()
print(obj.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
