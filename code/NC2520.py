class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 0
        tmpNum = num
        while tmpNum:
            oneNum = tmpNum % 10
            tmpNum //= 10
            if num % oneNum == 0:
               ret += 1

        return ret


obj = Solution()
print(obj.countDigits(7))
print(obj.countDigits(121))
print(obj.countDigits(1248))