class Solution(object):
    def isGoodArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果有数字的最大公约数为1则可以获得"好数组"
        divisor = nums[0]
        for num in nums:
            divisor = self.pub(divisor, num)
            if divisor == 1:
                break

        return divisor == 1

    # 最大公约数
    def pub(self, num1, num2):
        while num2 != 0:
            temp = num1
            num1 = num2
            num2 = temp % num2
        return num1


obj = Solution()
print(obj.isGoodArray([3,6]))