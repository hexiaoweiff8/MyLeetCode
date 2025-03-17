class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = n // 2
        leftVal = mid * (1 + mid) / 2
        rightVal = (n - mid + 1) * (mid + n) / 2
        # 二分法
        while left < right:
            if leftVal == rightVal:
                return mid
            if leftVal > rightVal:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2
            leftVal = mid * (1 + mid) / 2
            rightVal = (n - mid + 1) * (mid + n) / 2

        if leftVal == rightVal:
            return mid

        return -1


obj = Solution()
print(obj.pivotInteger(8))
print(obj.pivotInteger(1))
print(obj.pivotInteger(4))