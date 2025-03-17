class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        # len1, len2 = len(s1), len(s2)
        # index1, index2 = 0, 0
        # if len1 == 0 or len2 == 0 or len1 * n1 < len2 * n2:
        #     return 0
        # map1, map2 = {}, {}
        # ret = 0
        # while index1 // len1 < n1:
        #     if index1 % len1 == len1 - 1:
        #         val = map1.get(index2 % len2, None)
        #         if val:
        #             cycleLen = index1 // len1 - val // len1
        #             cycleNum = (n1 - 1 - index1 // len1) // cycleLen
        #             cycleS2Num = index2 // len2 - map2[index2 % len2] // len2
        #             index1 += cycleLen * cycleNum * len1
        #             ret += cycleS2Num * cycleNum
        #         else:
        #             map1[index2 % len2] = index1
        #             map2[index2 % len2] = index2
        #     if s1[index1 % len1] == s2[index2 % len2]:
        #         if index2 % len2 == len2 - 1:
        #             ret += 1
        #         index2 += 1
        #     index1 += 1

        # return ret // n2
        len1, len2 = len(s1), len(s2)
        map1, map2 = {}, {}
        index1, index2 = 0, 0
        ret = 0
        while index1 // len1 < n1:
            if index1 % len1 == len1 - 1:
                val = map1.get(index2 % len2, None)
                # 如果出现循环
                if val:
                    # 计算循环在s1中的长度
                    cycleLen = index1 // len1 - val // len1
                    # 计算剩下循环的数量
                    cycleNum = (n1 - 1 - index1 // len1) // cycleLen
                    # 计算每个循环包含s2的数量
                    cycleS2Num = index2 // len2 - map2[index2 % len2] // len2

                    # s1快进
                    index1 += cycleLen * cycleNum * len1
                    # 结果加入答案
                    ret += cycleS2Num * cycleNum
                else:
                    # 记录
                    map1[index2 % len2] = index1
                    map2[index2 % len2] = index2
            # index2 前进
            if s1[index1 % len1] == s2[index2 % len2]:
                if index2 % len2 == len2 - 1:
                    ret += 1
                index2 += 1
            index1 += 1




obj = Solution()
print(obj.getMaxRepetitions("acacacb", 4, "ab", 2))