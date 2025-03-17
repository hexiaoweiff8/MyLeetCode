class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        dic = {}
        for value, weight in items1 + items2:
            dic[value] = dic.get(value, 0) + weight

        ret = sorted([v1, v2] for v1, v2 in dic.items())
        return ret


obj = Solution()
print(obj.mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))
