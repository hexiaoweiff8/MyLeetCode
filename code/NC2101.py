import math


class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        bombs.sort(key=lambda item: item[2], reverse=True)
        n = len(bombs)

        ret = 0
        for i in range(n):
            history = [False] * n
            history[i] = True
            stack = [i]
            tmpRet = 0
            while stack:
                cur = stack.pop()
                for i in range(n):
                    if i == cur:
                        continue
                    if not history[i] and math.sqrt((bombs[cur][0] - bombs[i][0]) ** 2 + (bombs[cur][1] - bombs[i][1]) ** 2) <= bombs[cur][2]:
                        stack.append(i)
                        history[i] = True
                        tmpRet += 1

            ret = max(ret, tmpRet + 1)
        return ret


obj = Solution()
print(obj.maximumDetonation([[4,4,3],[4,4,3]]))
