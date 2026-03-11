class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        w = n.bit_length()
        return ((1 << w) - 1) ^ n
