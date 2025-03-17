class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 1位数4个, 2位数每十个5个, 3位数每十个5个
        bitCount = 1
        count = 0
        firstCount1 = 0
        firstCount2 = 0
        sumVal = 0
        idx = 0
        if num < 10:
            return num // 2
        while num > 0:
            val = num % 10
            num //= 10
            if idx == 0:
                # 处理个位
                for index in range(val + 1):
                    if index % 2 == 0:
                        firstCount1 += 1
                    else:
                        firstCount2 += 1
            else:
                count += 5 * val * bitCount
                sumVal += val
                bitCount *= 10
            idx += 1

        return count - 1 + (firstCount1 if sumVal % 2 == 0 else firstCount2)


obj = Solution()
print(obj.countEven(896))
print(obj.countEven(13))
print(obj.countEven(26))
print(obj.countEven(4))
print(obj.countEven(38))
print(obj.countEven(63))
print(obj.countEven(30))
print(obj.countEven(40))

# 896 447
# 13 6
# 26 13
# 4 2
# 38 18
# 63 31
# 30 14
