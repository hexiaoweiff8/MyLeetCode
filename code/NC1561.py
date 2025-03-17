class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # 取最大2个, 并取最小的一个数, 取中间一个数求和
        return sum(sorted(piles)[len(piles)//3::2])