import heapq


class Solution(object):
    def minimumVisitedCells(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # m, n = len(grid), len(grid[0])
        # if m == 1 and n == 1:
        #     return 1
        # dp = [[float('inf')] * (n) for _ in range(m)]
        # dp[0][0] = 0
        # dp[-1][-1] = 9999999999
        # for i in range(0, m):
        #     for j in range(0, n):
        #         for k in range(j + 1, min(grid[i][j] + j + 1, n)):
        #             dp[i][k] = min(dp[i][k], dp[i][j] + 1)
        #         for k in range(i + 1, min(grid[i][j] + i + 1, m)):
        #             dp[k][j] = min(dp[k][j], dp[i][j] + 1)
        # return (dp[-1][-1] + 1) if dp[-1][-1] != 9999999999 else -1
        colHeaps = [[] for _ in grid[0]]
        for i, row in enumerate(grid):
            rowHeap = []
            for j, (g, colHeap) in enumerate(zip(row, colHeaps)):
                while rowHeap and rowHeap[0][1] < j:
                    heapq.heappop(rowHeap)
                while colHeap and colHeap[0][1] < i:
                    heapq.heappop(colHeap)
                f = float("inf") if i or j else 1
                if rowHeap:
                    f = rowHeap[0][0] + 1
                if colHeap:
                    f = min(f, colHeap[0][0] + 1)
                if g and f < float("inf"):
                    heapq.heappush(rowHeap, [f, g + j])
                    heapq.heappush(colHeap, [f, g + i])
        return f if f < float("inf") else -1

obj = Solution()
# print(obj.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]))
# print(obj.minimumVisitedCells([[3, 4, 2, 1], [4, 2, 1, 1], [2, 1, 1, 0], [3, 4, 1, 0]]))
# print(obj.minimumVisitedCells([[2, 1, 0], [1, 0, 0]]))
print(obj.minimumVisitedCells([[0]]))
