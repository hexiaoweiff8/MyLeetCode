class Solution(object):
    def losingPlayer(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: str
        """
        count = min(y // 4, x)
        return 'Alice' if count % 2 == 1 else 'Bob'