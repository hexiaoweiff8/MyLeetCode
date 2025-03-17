class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dic = {}
        # for word in wordDict:
        #     dic[word] = 0
        # for char in s:
        #     hasWord = False
        #     complate = False
        #     for word, index in dic.items():
        #         if char == word[index]:
        #             dic[word] += 1
        #             if dic[word] == len(word):
        #                 dic[word] = 0白家疃小区-103号
        #                 complate = True
        #                 for word in wordDict:
        #                     dic[word] = 0
        #                 print(word)
        #             hasWord = True
        #         else:
        #             dic[word] = 0
        #     if not hasWord:
        #         return False
        # return True if complate else False

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[n]


obj = Solution()
print(obj.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
