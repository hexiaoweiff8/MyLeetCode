from collections import defaultdict


class Solution(object):
    def maxPointsInsideSquare(self, points, s):
        """
        :type points: List[List[int]]
        :type s: str
        :rtype: int
        """
        key = defaultdict(list)
        for i, (x, y) in enumerate(points):
            key[max(abs(x), abs(y))].append(i)
        ret = 0
        history = set()
        for val in sorted(key):
            idx = key[val]
            for i in idx:
                if s[i] in history:
                    return ret
                history.add(s[i])
            ret += len(idx)

        return ret


obj = Solution()
print(obj.maxPointsInsideSquare([[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], "abdca"))
