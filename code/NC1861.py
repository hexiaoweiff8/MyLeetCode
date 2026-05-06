class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        n, m = len(boxGrid), len(boxGrid[0])

        for i in range(n):
            j = m - 1
            while j > 0:
                if boxGrid[i][j] == '.':
                    # 向前移动, 遇到# 将#移动到当前为止, 遇到*则 j = *的位置-1
                    k = j - 1
                    while k >= 0:
                        if boxGrid[i][k] == '#':
                            boxGrid[i][j], boxGrid[i][k] = boxGrid[i][k], boxGrid[i][j]
                            break
                        elif boxGrid[i][k] == '*':
                            j = k
                            break
                        else:
                            k -= 1

                    j -= 1
                else:
                    j -= 1
        # 顺时针旋转90度：先转置，再反转每一行
        rotated = list(map(list, zip(*boxGrid)))
        for row in rotated:
            row.reverse()
        return rotated


obj = Solution()
print(obj.rotateTheBox([["#", ".", "#"]]))
print(obj.rotateTheBox([["#", ".", "*", "."],
                        ["#", "#", "*", "."]]))
print(
    obj.rotateTheBox([["#", "#", "*", ".", "*", "."],
                      ["#", "#", "#", "*", ".", "."],
                      ["#", "#", "#", ".", "#", "."]]))
