class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        # 获取一个人可以获得最长的字符串
        n = len(word)
        maxLen = n - numFriends + 1
        maxStr = word[:maxLen]
        for i in range(maxLen, n + maxLen):
            # 删除第一个字符, 添加一个字符, 如果没有字符填就减少长度
            maxStr = max(maxStr, word[i - maxLen + 1:min(n, i + 1)])

        return maxStr


obj = Solution()
print(obj.answerString("gh", 1))