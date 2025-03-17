class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 获取车的位置
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        # 上下左右延伸计数第一个遇到的卒
        array = [0, 0, 0, 0]
        for i in range(8):
            if board[max(x - i, 0)][y] == 'p' and array[0] != 2:
                array[0] = 1
            elif board[max(x - i, 0)][y] == 'B' and array[0] != 1:
                array[0] = 2
            if board[min(x + i, 7)][y] == 'p' and array[1] != 2:
                array[1] = 1
            elif board[min(x + i, 7)][y] == 'B' and array[1] != 1:
                array[1] = 2
            if board[x][max(y - i, 0)] == 'p' and array[2] != 2:
                array[2] = 1
            elif board[x][max(y - i, 0)] == 'B' and array[2] != 1:
                array[2] = 2
            if board[x][min(y + i, 7)] == 'p' and array[3] != 2:
                array[3] = 1
            elif board[x][min(y + i, 7)] == 'B' and array[3] != 1:
                array[3] = 2
        # 判断ans中1的数量, 排除2的数量
        ans = 0
        for i in array:
            if i == 1:
                ans += 1
        return ans


obj = Solution()
print(obj.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                           [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                           [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                           [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
