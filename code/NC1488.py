from sortedcontainers import SortedList

class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        # 记录没有满足条件的雨水
        empty = SortedList()
        # 记录没有满足条件的雨水对应的地方
        full_dict = {}
        res = []
        for i, rain in enumerate(rains):
            if rain == 0:
                empty.add(i)
                res.append(1)
            else:
                if rain in full_dict:
                    # 如果有满足条件的雨水，就找到对应的地方
                    # 查找empty中是否有在两个full中间的索引
                    emptyIndex = empty.bisect(full_dict[rain])
                    if emptyIndex == len(empty):
                        return []
                    emptyIndex = empty[emptyIndex]
                    res[emptyIndex] = rain
                    empty.remove(emptyIndex)
                full_dict[rain] = i
                res.append(-1)
        return res


obj = Solution()
# print(obj.avoidFlood([1, 2, 3, 4]))
print(obj.avoidFlood([1, 2, 0, 0, 2, 1]))
# print(obj.avoidFlood([1, 2, 0, 1, 2]))
print(obj.avoidFlood([69, 0, 0, 0, 69]))
# print(obj.avoidFlood([1, 1, 0, 0]))
# print(obj.avoidFlood([1, 2, 0, 2, 3, 0, 1]))
# print(obj.avoidFlood([1, 3, 2, 0, 2, 0, 3, 0, 1, 0, 0, 0]))
print(obj.avoidFlood([0, 1, 1]))
