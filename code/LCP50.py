class Solution(object):
    def giveGem(self, gem, operations):
        """
        :type gem: List[int]
        :type operations: List[List[int]]
        :rtype: int
        """
        for operate in operations:
            val = gem[operate[0]] // 2
            gem[operate[1]] += val
            gem[operate[0]] -= val
        return max(gem) - min(gem)


obj = Solution()
print(obj.giveGem(gem=[100, 0, 50, 100], operations=[[0, 2], [0, 1], [3, 0], [3, 0]]))
