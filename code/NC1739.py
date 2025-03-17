# 有一个立方体房间，其长度、宽度和高度都等于 n 个单位。请你在房间里放置 n 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下：
#
# 你可以把盒子放在地板上的任何地方。
# 如果盒子 x 需要放置在盒子 y 的顶部，那么盒子 y 竖直的四个侧面都 必须 与另一个盒子或墙相邻。
# 给你一个整数 n ，返回接触地面的盒子的 最少 可能数量。

class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1+2+3+4
        index = 1
        index2 = 1
        sum = 0
        sum2 = 0
        allSum = 0
        preSum = 0
        preAllSum = 0
        while True:
            preSum = sum
            sum += index
            preAllSum = allSum
            allSum += sum
            index += 1
            if allSum > n:
                subVal = n - preAllSum
                # 将该值按照三角形左下角聚集进位
                while True:
                    sum2 += index2
                    index2 += 1
                    if sum2 >= subVal:
                        return (index2 - 1) + preSum

            elif allSum == n:
                return sum


obj = Solution()
print(obj.minimumBoxes(275))
