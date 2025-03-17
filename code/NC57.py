class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 1. 先找到插入位置
        # 2. 插入
        # 3. 合并
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res


obj = Solution()
print(obj.insert([[1, 3], [6, 9]], [2, 5]))