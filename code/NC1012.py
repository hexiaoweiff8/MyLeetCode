import math


class Solution(object):
    def numDupDigitsAtMostN(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 判断高位是否可包含
        # valDic = {}
        # plusDic = {1: [0, 0],
        #            10: [0, 1],
        #            100: [10, 28], # 18
        #            1000: [262, 496], # 234
        #            10000: [4726, 6976], # 2250
        #            100000: [67510, 84880], # 17370
        #            1000000: [831430, 939520], # 108090
        #            10000000: [9287110, 9818560], # 531450
        #            100000000: [97654150, 99637120], # 1982970
        #            1000000000: [994388230, 0]
        #            }

        ret = 0
        now = 0
        sumSkipNum = 0
        while now <= n:
            # 最后一个跨越问题 如果跨越范围超过最终值, 则需要缩小跨越范围.
            skipNum = self.checkJump(now, n)
            # 判断是否支持跳过, 如果跳过跳过多少, 从大位数开始判断, 如果跳过则增加大位数值
            if skipNum:
                now += skipNum
                ret += skipNum
                sumSkipNum += skipNum
            else:
                dic = {}
                # 校验numCountList是否包含多个相同值
                # 按照相同的值为主
                tmpNow = now
                while tmpNow > 0:
                    bit = tmpNow % 10
                    tmpNow //= 10
                    dic[bit] = dic.get(bit, 0) + 1
                    if dic[bit] > 1:
                        ret += 1
                        break

                now += 1
        print("跳过", sumSkipNum)
        return ret

    # 检查是否跳过
    def checkJump(self, num, max):
        if num:
            sourceNum = num
            numLen = len(str(num)) - 1
            maxMutil = int(math.pow(10, numLen))
            dicLocal = {}
            while maxMutil > 0:
                bit = num // maxMutil
                num = num % maxMutil
                dicLocal[bit] = dicLocal.get(bit, 0) + 1
                if dicLocal[bit] > 1 and sourceNum + maxMutil <= max:
                    break
                maxMutil //= 10
                numLen -= 1
            return maxMutil
        return 0


obj = Solution()
# print(obj.numDupDigitsAtMostN(100))
print(obj.numDupDigitsAtMostN(5987490))
# print(obj.numDupDigitsAtMostN(10000))
