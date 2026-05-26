class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        ans = 0
        dic = {}
        for i in range(len(word)):
            # 判断是否为小写
            if word[i].lower() not in dic:
                dic[word[i].lower()] = {"islower": word[i].islower(), "isDone": False}
            elif not dic[word[i].lower()]["isDone"] and dic[word[i].lower()]["islower"] != word[i].islower():
                dic[word[i].lower()]["isDone"] = True
                ans += 1
        return ans

