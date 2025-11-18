class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)

        index = 0
        while index < n - 1:
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return index == n - 1
