class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        pairs = sorted(zip(aliceValues, bobValues), key=lambda x: -x[0] - x[1])
        diff = sum(x if i % 2 == 0 else -y for i, (x, y) in enumerate(pairs))
        return (diff > 0) - (diff < 0)
