"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：
nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。
注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

示例 1：
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。

示例 2：
输入：n = 6, index = 1,  maxSum = 10
输出：3
"""


class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        leftCount = index
        rightCount = n - index - 1
        # minScope = min(leftCount, rightCount)
        # 二分法处理
        # 处理左侧求和, 处理右侧求和, 若大于maxSum则增值/2, 否则继续增加
        # 对n[index]去maxSum进行二分法处理, 分别确定两侧山峰值
        leftVal, rightVal = 1, maxSum
        while leftVal < rightVal:
            mid = (leftVal + rightVal + 1) // 2
            # 如果计算值大于maxSum则往左区间便宜, 否则往右区间偏移
            if mid + self.cal(mid, leftCount) + self.cal(mid, rightCount) <= maxSum:
                leftVal = mid
            else:
                rightVal = mid - 1

        return leftVal

    # 计算左右山峰值
    def cal(self, mid, count):
        if count + 1 < mid:
            # 计算纯山坡
            return (mid * 2 - count - 1) * count // 2
        else:
            # 计算山峰+平路
            return (count - mid + 1) + (mid - 1 + 1) * (mid - 1) // 2


obj = Solution()
print(obj.maxValue(6, 1, 10))
