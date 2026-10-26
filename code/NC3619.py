class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        indexSet = set()
        ans = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    if (i, j) not in indexSet:
                        sumVal = cell
                        indexSet.add((i, j))
                        stack = [(i, j)]
                        while stack:
                            x, y = stack.pop()
                            for dx, dy in dir:
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] and (nx, ny) not in indexSet:
                                    indexSet.add((nx, ny))
                                    stack.append((nx, ny))
                                    sumVal += grid[nx][ny]

                        if sumVal % k == 0:
                            ans += 1

        return ans

