class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [999999999]
        ret = 0
        for x in arr:
            while x >= stack[-1]:
                ret += stack.pop() * min(stack[-1], x)
            stack.append(x)
        while len(stack) > 2:
            ret += stack.pop() * stack[-1]
        return ret
        # count = nLen = len(arr)
        # # 计算层数
        # level = 0
        # while nLen != 0:
        #     level += 1
        #     nLen //= 2
        # # 处理每个节点所在层数
        # levelCount = pow(2, level - 1)
        # subCount = count - levelCount
        # # 下层数量
        # subCount *= 2
        # stack = []
        # maxStack = []
        # ret = 0
        # stack.extend(arr[:-subCount if subCount != 0 else count])
        # maxStack.extend(arr[:-subCount if subCount != 0 else count])
        # for index in range(0, subCount, 2):
        #     # 处理下层乘积
        #     stack.append(arr[-subCount + index] * arr[-subCount + index + 1])
        #     maxStack.append(max(arr[-subCount + index], arr[-subCount + index + 1]))
        # ret += sum(stack[:subCount])
        # print(stack)
        # while len(stack) > 1:
        #     tmpStack = []
        #     tmpMaxStack = []
        #     for index in range(0, len(stack), 2):
        #         tmpStack.append(maxStack[index] * maxStack[index + 1])
        #         tmpMaxStack.append(max(maxStack[index], maxStack[index + 1]))
        #     stack = tmpStack
        #     maxStack = tmpMaxStack
        #     ret += sum(stack)
        #     print(stack)
        # return ret


obj = Solution()
print(obj.mctFromLeafValues([15, 13, 5, 3, 15]))
print(obj.mctFromLeafValues([6, 2, 4]))
print(obj.mctFromLeafValues([4, 11]))
