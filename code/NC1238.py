import math


class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """
        ret = [0] * (1 << n)
        for index in range(1 << n):
            ret[index] = (index >> 1) ^ index ^ start
        return ret
    #     count = int(math.pow(2, n) - 1)
    #     binCount = self.getBinCount(count)
    #     ret = [0]
    #     # 将数字先进行间隔差异排序, 然后start为第一个切取环
    #     # 左侧插入1000 右侧插入0001 然后
    #     leftInsertVal = int(math.pow(2, n - 1))
    #     rightInserVal = 1
    #     for index in range(binCount):
    #         ret.append(rightInserVal)
    #         ret.insert(0, leftInsertVal)
    #         leftInsertVal += int(math.pow(2, index))
    #         rightInserVal += int(math.pow(2, index + 1))
    #
    #     # 删除最后一个重复内容
    #     ret = ret[: -1]
    #     # 补充两端内容
    #
    #     print(ret)
    #     index = ret.index(start)
    #     # 调整list顺序
    #     return ret[index:] + ret[:index]
    #
    # def getBinCount(self, count):
    #     """
    #     计算二进制数量
    #     :param count:
    #     :return:
    #     """
    #     ret = 0
    #     while count > 0:
    #         count //= 2
    #         ret += 1
    #     return ret



obj = Solution()
print(obj.circularPermutation(3, 2))
