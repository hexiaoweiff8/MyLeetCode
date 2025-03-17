class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        return 100 - ((purchaseAmount // 10) * 10 + (10 if (purchaseAmount % 10) >= 5 else 0))