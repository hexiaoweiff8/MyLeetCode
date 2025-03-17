import copy


class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        # 快捷处理
        n -= 1
        if a == b:
            return a * (n + 1) % 1000000007

        # 计算最大公约数
        max_pub = self.pub(a, b)
        val1 = a // max_pub
        val2 = b // max_pub
        # 获取小的那个值设置到val1
        if val1 > val2:
            tmp = val2
            val2 = val1
            val1 = tmp

        if val1 == 1:
            return max_pub * (n + 1) % 1000000007

        # scope内序列规律
        # 计算区间范围
        # 5 6 1 22222
        # 5 7 2 22322
        # 5 8 3 23232
        # 5 9 4 23332
        # 5 11 6 33333
        # 8 9 1 22222222
        # 8 11 3 22233222
        # 8 13 5 22333322
        # 8 15 7 23333332
        # 8 17 9 33333333
        # 每val1+val2-1个值一个循环从val1的倍数开始val1的倍数结束
        cycleCount = val1 + val2 - 1
        scope = n // cycleCount
        scopeIdx = n % cycleCount
        scopeMutil = 2
        subVal = val2 - val1
        # 整倍数退位
        # if subVal % val1 == 1:
        #     scopeMutil -= 1
        subVal2 = subVal - 1
        scopeArray = [scopeMutil] * (val1 // 2 + (val1 % 2))
        scopePosArray = []
        scopeArrayLastIndex = len(scopeArray) - 1
        scoreVal1Val2Array2 = []
        if val1 % 2 == 0:
            subVal2 -= 1
        # 特殊进位控制
        while subVal2 > 0:
            scopeArray[0] += 1
            if scopeArray[0] - scopeArray[scopeArrayLastIndex] >= 2:
                for index in range(1, scopeArrayLastIndex + 1):
                    if scopeArray[0] - scopeArray[index] == 2:
                        scopeArray[index] += 1
                        break
                scopeArray[0] -= 2
            subVal2 -= 1

        # 区分奇偶数
        if val1 % 2 == 0:
            # 数组翻转倍增
            resScorpArray = copy.deepcopy(scopeArray)
            resScorpArray.reverse()
            resScorpArray.extend(scopeArray)
        else:
            resScorpArray = copy.deepcopy(scopeArray)
            resScorpArray.reverse()
            resScorpArray.pop()
            resScorpArray.extend(scopeArray)

        pos = 0
        for val in resScorpArray:
            for index in range(val):
                if index >= val - 1:
                    scopePosArray.append((pos, 1))
                    scoreVal1Val2Array2.append(1)
                else:
                    scopePosArray.append((pos, 0))
                    scoreVal1Val2Array2.append(0)
            pos += 1

        scopeArrayIndex, isLast = scopePosArray[scopeIdx]
        if isLast == 1:
            finalVal = (scopeArrayIndex + 1) * val2
        else:
            # 合并所有前置-1
            finalVal = (scopeIdx + 1 - scopeArrayIndex) * val1

        scopeValArray = []
        scoreVal1Val2Array = []
        # 构建单循环内所有值
        for index in range(1, val1 + 1):
            scopeValArray.append(val2 * index)

        for index in range(1, val2 + 1):
            scopeValArray.append(val1 * index)

        scopeValArray.sort()
        for val in scopeValArray:
            if val / val1 == val // val1:
                scoreVal1Val2Array.append(0)
            else:
                scoreVal1Val2Array.append(1)
        print(scopeValArray)
        print(scoreVal1Val2Array)
        print(scoreVal1Val2Array2)
        print(scopeValArray[scopeIdx])

        # 计算倍数 总区间 + 小区间 + 小区间位置
        return (val1 * val2 * max_pub * scope + finalVal * max_pub) % 1000000007

    # 最大公约数
    def pub(self, num1, num2):
        while num2 != 0:
            temp = num1
            num1 = num2
            num2 = temp % num2
        return num1


obj = Solution()
print(obj.nthMagicalNumber(136, 139, 146))
# 10 9 4 28
# 3 6 4 8
# 3 8 3 8
#136 556 584 38920