class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        x, y = ord(coordinates[0]) - ord('a') + 1, int(coordinates[1])
        return (x + y) % 2 == 1