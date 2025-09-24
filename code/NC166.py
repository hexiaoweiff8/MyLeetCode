class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        res = sign + str(numerator // denominator)
        if numerator % denominator == 0:
            return res
        res += '.'
        numerator %= denominator

        # 记录余数的位置
        pos = {}
        while numerator:
            if numerator in pos:
                res = res[:pos[numerator]] + '(' + res[pos[numerator]:] + ')'
                return res
            pos[numerator] = len(res)
            numerator *= 10
            res += str(numerator // denominator)
            numerator %= denominator
        return res

