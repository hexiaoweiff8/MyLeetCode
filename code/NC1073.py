import math


class Solution:
    def addNegabinary(self, arr1, arr2):
        val = 0
        arr1Len, arr2Len = len(arr1), len(arr2)
        for index in range(arr1Len):
            if arr1[index]:
                val += int(math.pow(-2, arr1Len - 1 - index))

        for index in range(arr2Len):
            if arr2[index]:
                val += int(math.pow(-2, arr2Len - 1 - index))

        # 计算结果
        ret = []
        while val != 0:
            ret.insert(0, val & 1)
            val = (val - (val & 1)) // -2
        if not ret:
            return [0]


obj = Solution()
print(obj.addNegabinary(arr1=[1, 1, 1, 1, 1], arr2=[1, 0, 1]))
print(obj.addNegabinary(arr1=[0], arr2=[0]))
print(obj.addNegabinary(arr1=[0], arr2=[1]))
print(obj.addNegabinary(arr1=[0], arr2=[1, 0]))
print(obj.addNegabinary(arr1=[0], arr2=[1, 1]))
