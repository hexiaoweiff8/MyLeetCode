from functools import reduce


class Solution(object):
    def maximumRows(self, matrix, numSelect):
        """
        :type matrix: List[List[int]]
        :type numSelect: int
        :rtype: int
        """
        rows = []
        for row in matrix:
            mask = reduce(lambda x, y: x | y, (1 << j for j, x in enumerate(row) if x), 0)
            rows.append(mask)
        ret = 0
        for mask in range(1 << len(matrix[0])):
            cnt = bin(mask).count('1')
            if cnt == numSelect:
                ret = max(ret, sum(x & mask == x for x in rows))

        return ret


obj = Solution()
# print(obj.maximumRows(matrix=[[0, 0, 0],
#                               [1, 0, 1],
#                               [0, 1, 1],
#                               [0, 0, 1]], numSelect=2))
print(obj.maximumRows(matrix=[[1, 0, 1, 1, 1, 1],
                              [0, 0, 0, 1, 1, 0],
                              [1, 1, 0, 0, 0, 0],
                              [0, 0, 1, 1, 0, 1]], numSelect=2))
