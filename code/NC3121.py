class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        dic = {}
        for c in word:
            if dic.get(c.lower(), True):
                lst = dic.get(c.lower(), [])
                dic[c.lower()] = lst
                if len(lst) > 1:
                    if lst[-1].isupper() and c.islower():
                        dic[c.lower()] = False
                    else:
                        lst.append(c)
                else:
                    lst.append(c)

        # 返回所有结果为2的
        return sum(1 for k, v in dic.items() if v and len(v) > 1 and v[-1].isupper() and v[0].islower())


obj = Solution()
print(obj.numberOfSpecialChars("AbBCab"))