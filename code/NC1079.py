from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        count = Counter(tiles)
        tileSet = set(tiles)

        def dfs(i):
            if i == 0:
                return 1
            res = 1
            for t in tileSet:
                if count[t] > 0:
                    count[t] -= 1
                    res += dfs(i - 1)
                    count[t] += 1
            return res

        return dfs(len(tiles)) - 1


obj = Solution()
print(obj.numTilePossibilities("AAAAAA"))
