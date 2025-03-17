class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        dictTarget = {}
        dictS = {}
        for char in target:
            dictTarget[char] = dictTarget.get(char, 0) + 1

        for char in s:
            if char in dictTarget:
                dictS[char] = dictS.get(char, 0) + 1

        # 匹配最小倍数
        minCount = 99999999
        for key in dictTarget.keys():
            targetCount = dictTarget.get(key)
            if key in dictS:
                sCount = dictS[key]
                multi = sCount // targetCount
                if multi < minCount:
                    minCount = multi
            else:
                return 0
        return minCount


obj = Solution()
print(obj.rearrangeCharacters('abbaccaddaeea', "aaaaa"))
