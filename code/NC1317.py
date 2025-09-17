class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def has_no_zero(num):
            """检查数字是否不包含0"""
            return '0' not in str(num)
        
        for a in range(1, n):
            b = n - a
            if has_no_zero(a) and has_no_zero(b):
                return [a, b]
        return [0, 0]  # 理论上不会执行到这里，因为至少有一个解


obj = Solution()
print(obj.getNoZeroIntegers(11))
print("2:", obj.getNoZeroIntegers(2))
print("10:", obj.getNoZeroIntegers(10))
print("100:", obj.getNoZeroIntegers(100))
