#给你一个字符串 s ，由 n 个字符组成，每个字符不是 'X' 就是 'O' 。
#一次 操作 定义为从 s 中选出 三个连续字符 并将选中的每个字符都转换为 'O' 。注意，如果字符已经是 'O' ，只需要保持 不变 。
#返回将 s 中所有字符均转换为 'O' 需要执行的最少操作次数。

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 遍历s, 窗口右移, 窗口长度3, 窗口左侧为X时则进行转换并计数
        count = 0
        strLen = len(s)
        index = 0
        while index < strLen:
            char = s[index]
            if char == 'X':
                count += 1
                index += 3
            else:
                index += 1

        return count

obj = Solution()
print(obj.minimumMoves('OOOO'))
