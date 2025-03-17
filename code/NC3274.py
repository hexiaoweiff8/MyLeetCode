class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        x1, y1 = int(coordinate1[1:]), ord(coordinate1[0])
        x2, y2 = int(coordinate2[1:]), ord(coordinate2[0])
        return (x1 + y1) & 1 == (x2 + y2) & 1