class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = ""
        num, carry = 0, 0
        len1, len2 = len(num1), len(num2)
        for index in range(1, max(len1, len2) + 1):
            if index <= len1:
                num += int(num1[-index])
            if index <= len2:
                num += int(num2[-index])
            num += carry
            if num >= 10:
                carry = 1
                num -= 10
            else:
                carry = 0
            ret = str(num) + ret
            num = 0
        if carry:
            ret = "1" + ret
        return ret


obj = Solution()
# print(obj.addStrings(num1 = "11", num2 = "123"))
# print(obj.addStrings(num1 = "456", num2 = "77"))
# print(obj.addStrings(num1 = "0", num2 = "0"))
print(obj.addStrings(num1 = "1", num2 = "9"))