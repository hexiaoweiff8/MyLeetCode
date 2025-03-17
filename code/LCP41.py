class Solution(object):
    def flipChess(self, chessboard):
        """
        :type chessboard: List[str]
        :rtype: int
        """
        ret = 0
        dirs = [(a, b) for a in range(-1, 2) for b in range(-1, 2) if a != 0 or b != 0]
        m, n = len(chessboard), len(chessboard[0])
        for rowStr in chessboard:
            # 获取O附近的位置
            # 计算这些位置
            for char in rowStr:
                if char == ".":
                    # 遍历附近位置
                elif char == "X":
                    pass
                elif char == "O":
                    pass

        return ret


obj = Solution()
print(obj.flipChess(["....X.", "....X.", "XOOO..", "......", "......"]))
print(obj.flipChess([".X.", ".O.", "XO."]))
print(obj.flipChess([".......", ".......", ".......", "X......", ".O.....", "..O....", "....OOX"]))
