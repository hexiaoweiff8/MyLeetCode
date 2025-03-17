from collections import Counter


class Solution(object):
    def equalPairs(self, grid):
        res, n = 0, len(grid)
        cnt = Counter(tuple(row) for row in grid)
        res = 0
        for j in range(n):
            res += cnt[tuple([grid[i][j] for i in range(n)])]
        return res


obj = Solution()
# print(obj.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
# print(obj.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
# print(obj.equalPairs([[3,1,2,2],
#                       [1,4,4,4],
#                       [2,4,2,2],
#                       [2,5,2,2]]))
# print(obj.equalPairs([[3,1,2,2],
#                       [1,4,4,5],
#                       [2,4,2,2],
#                       [2,4,2,2]]))

print(obj.equalPairs([[13,13],
                      [13,13]]))