class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(grid), len(grid[0])
        minHalf = min(n, m) // 2
        
        # 创建结果矩阵
        result = [[0] * m for _ in range(n)]
        
        # 对每一层进行处理
        for deep in range(minHalf):
            # 提取当前层的所有元素
            elements = []
            
            # 上边（从左到右）
            for i in range(deep, m - deep):
                elements.append(grid[deep][i])
            
            # 右边（从上到下，不包括右上角）
            for i in range(deep + 1, n - deep):
                elements.append(grid[i][m - deep - 1])
            
            # 下边（从右到左，不包括右下角）
            for i in range(m - deep - 2, deep - 1, -1):
                elements.append(grid[n - deep - 1][i])
            
            # 左边（从下到上，不包括左下角和左上角）
            for i in range(n - deep - 2, deep, -1):
                elements.append(grid[i][deep])
            
            # 计算旋转后的位置
            length = len(elements)
            effective_k = k % length  # 避免不必要的完整循环
            
            # 将旋转后的元素放回对应位置
            idx = 0
            
            # 上边
            for i in range(deep, m - deep):
                result[deep][i] = elements[(idx + effective_k) % length]
                idx += 1
            
            # 右边
            for i in range(deep + 1, n - deep):
                result[i][m - deep - 1] = elements[(idx + effective_k) % length]
                idx += 1
            
            # 下边
            for i in range(m - deep - 2, deep - 1, -1):
                result[n - deep - 1][i] = elements[(idx + effective_k) % length]
                idx += 1
            
            # 左边
            for i in range(n - deep - 2, deep, -1):
                result[i][deep] = elements[(idx + effective_k) % length]
                idx += 1
        
        return result


obj = Solution()
print(obj.rotateGrid([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 1))
