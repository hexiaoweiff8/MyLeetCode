from collections import Counter


class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        dic = {a for a, b in zip(fronts, backs) if a == b}
        return min((x for x in fronts + backs if x not in dic), default=0)

obj = Solution()
print(obj.flipgame(fronts=[1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3]))
print(obj.flipgame(fronts=[1], backs=[1]))
