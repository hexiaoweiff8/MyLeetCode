class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # 滑动窗口
        halfK = k // 2
        boder = 0 if k % 2 else 1
        minCount = nowCount = blocks[:k].count("W")
        for index in range(halfK, len(blocks) - halfK - 1 + boder):
            if blocks[index - halfK] == "W":
                nowCount -= 1
            if blocks[index + halfK + 1 - boder] == "W":
                nowCount += 1

            if minCount > nowCount:
                minCount = nowCount

        if minCount == 9999999:
            return nowCount
        return minCount


obj = Solution()
# print(obj.minimumRecolors("WBBWWBBWBW", 6))
# print(obj.minimumRecolors("WBWBBBW", 2))
# print(obj.minimumRecolors("BWWWBB", 6))
# print(obj.minimumRecolors("WWBBBWBBBBBWWBWWWB", 16))
print(obj.minimumRecolors("BBBBBWWBBWBWBWWWBWBWBBBBWBBBBWBWBWBWBWWBWWBWBWWWWBBWWWWBWWWWBWBBWBBWBBWWW", 29))
