class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        mLen = len(maxHeights)
        # 左侧找一遍
        # 右侧找一遍
        leftSumList = [0] * (mLen + 1)
        leftHeap = [mLen]
        leftSum = 0
        for i in range(mLen - 1, -1, -1):
            # 计算前置数值是否是相等或上升的
            height = maxHeights[i]
            while len(leftHeap) > 1 and maxHeights[leftHeap[-1]] >= height:
                j = leftHeap.pop()
                leftSum -= maxHeights[j] * (leftHeap[-1] - j)
            leftSum += height * (leftHeap[-1] - i)
            leftHeap.append(i)
            leftSumList[i] = leftSum
        rightSum = 0
        rightHeap = [-1]
        ret = leftSum
        for i, height in enumerate(maxHeights):
            # 计算后置数值是否是相等或下降的
            while len(rightHeap) > 1 and maxHeights[rightHeap[-1]] >= height:
                j = rightHeap.pop()
                rightSum -= maxHeights[j] * (j - rightHeap[-1])
            rightSum += height * (i - rightHeap[-1])
            rightHeap.append(i)
            ret = max(ret, leftSumList[i + 1] + rightSum)
        return ret





obj = Solution()
print(obj.maximumSumOfHeights([5, 3, 4, 1, 1]))
print(obj.maximumSumOfHeights([6, 5, 3, 9, 2, 7]))
print(obj.maximumSumOfHeights([3, 2, 5, 5, 2, 3]))
print(obj.maximumSumOfHeights([3, 5, 3, 5, 1, 5, 4, 4, 4]))
