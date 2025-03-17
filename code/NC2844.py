class Solution(object):
    def minimumOperations(self, num):
        """
        :type num: str
        :rtype: int
        """
        # 找到结尾, 四种情况, 结尾为00,25,50,75的情况, 如果都不符合则全部删除
        ret = 0
        hasFine = hasZero = hasVal = False
        zeroCount = 0
        for i in range(len(num) - 1, -1, -1):
            if (hasFine and (num[i] == '2' or num[i] == '7')) \
                    or (hasZero and (num[i] == '0' or num[i] == '5')):
                hasVal = True
                break
            if not hasZero and num[i] == '0':
                hasZero = True
            if not hasFine and num[i] == '5':
                hasFine = True
            if num[i] == '0':
                zeroCount += 1
            ret += 1
        return ret - (1 if hasVal else zeroCount)


obj = Solution()
# print(obj.minimumOperations("2245047"))
# print(obj.minimumOperations("2908305"))
# print(obj.minimumOperations("10"))
print(obj.minimumOperations("1"))