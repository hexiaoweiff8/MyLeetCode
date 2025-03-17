class Solution(object):
    def mergeStones(self, stones, k):
        """
        :type stones: List[int]
        :type k: int
        :rtype: int
        """
        # 判断-1情况
        stonesLen = len(stones)
        if (stonesLen - 1) % (k - 1) != 0:
            return - 1
        countList = []
        kSumList = []
        # 合并k个内容后, 查找最小集合
        for stone in stones:
            countList.append(stone)
            if len(countList) == k:
                countList.pop(0)
                kSumList.append(sum(countList))





obj = Solution()
print(obj.mergeStones([3, 2, 4, 1], 3))
