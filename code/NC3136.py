class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 3:
            return False
        yuanChar = set('aeiouAEIOU')
        yuanFlag = notYanFlag = False

        for c in word:
            # 判断是否只包含数字和大小写字母
            if not c.isalpha() and not c.isdigit():
                return False
            if c.isalpha():
                if c not in yuanChar:
                    notYanFlag = True
                else:
                    yuanFlag = True
        return yuanFlag and notYanFlag


obj = Solution()
print(obj.isValid("UuE6"))