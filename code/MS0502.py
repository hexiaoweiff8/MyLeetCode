class Solution(object):
    def printBin(self, num):
        """
        :type num: float
        :rtype: str
        """
        count = 0
        ret = '0.'
        while num != 0:
            num *= 2
            if num >= 1:
                num -= 1
                ret += "1"
            else:
                ret += "0"
            count += 1
            if count >= 32:
                return "ERROR"

        return ret

obj = Solution()
print(obj.printBin(0.1))
