from collections import Counter


class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 公式化简方式 i + rev(j) = j + rev(i)
        # 等同于 i - rev(i) = j - rev(j)
        # 循环数字进入, 数字做预处理并匹配合适数字, 返回最终结果
        cnt = Counter(x - self.rev(x) for x in nums)
        return sum(v * (v - 1) // 2 for v in cnt.values()) % 1000000007

    # 翻转数字
    def rev(self, x):
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        return y


obj = Solution()
print(obj.countNicePairs([42, 11, 1, 97]))
