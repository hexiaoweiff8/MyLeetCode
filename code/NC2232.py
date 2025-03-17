class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        left, right = expression.split('+')
        lenLeft, lenRight = len(left), len(right)
        minVal = int(left) + int(right)
        minIndexLeft, minIndexRight = 0, len(expression)
        for index in range(lenLeft):
            for index2 in range(1, lenRight + 1):
                tmpVal = int(left[:index] if index > 0 else "1") * (int(left[index:]) + int(right[:index2])) * int(right[index2:] if index2 < lenRight else "1")
                if tmpVal < minVal:
                    minVal = tmpVal
                    minIndexLeft, minIndexRight = index, index2

        # print(minVal)
        return left[:minIndexLeft] + "(" + left[minIndexLeft:] + "+" + right[:minIndexRight] + ")" + right[minIndexRight:]


obj = Solution()
print(obj.minimizeResult("247+38"))
print(obj.minimizeResult("12+34"))
print(obj.minimizeResult("999+999"))
