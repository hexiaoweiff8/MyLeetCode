class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        pre = num[0]
        index = 0
        maxVal = -1
        for i in range(1, len(num)):
            if index == 2:
                maxVal = max(maxVal, int(pre))
                index = 0
            if num[i] == pre:
                index += 1
            else:
                pre = num[i]
                index = 0

        if index == 2:
            maxVal = max(maxVal, int(pre))
        return str(maxVal) * 3 if maxVal >= 0 else ""


obj = Solution()
print(obj.largestGoodInteger("222"))