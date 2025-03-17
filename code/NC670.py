class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numLen = len(str(num))
        # 逐级处理最大值, 判断他们的站位是否是最大
        numStrList = list(str(num))
        numSet = set(numStrList)
        for i in range(9, -1, -1):
            if str(i) in numSet:
                maxIndex = numLen - numStrList[::-1].index(str(i)) - 1
                for j in range(maxIndex):
                    if numStrList[j] < numStrList[maxIndex]:
                        numStrList[j], numStrList[maxIndex] = numStrList[maxIndex], numStrList[j]
                        return int(''.join(numStrList))
        return num


object = Solution()
print(object.maximumSwap(2736))
print(object.maximumSwap(98368))