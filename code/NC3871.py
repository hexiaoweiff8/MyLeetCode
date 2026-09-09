class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1-999 1000-999999 1000000-999999999
        strNum = str(n)
        strCnt = len(strNum)
        maxCount = strCnt // 3 - (0 if strCnt % 3 else 1)
        ans = 0
        preMax = 999
        index = 0
        for index in range(1, maxCount):
            maxVal = pow(10, (index + 1) * 3) - 1
            ans += (maxVal - preMax) * index
            preMax = maxVal
        if n > preMax:
            ans += (n - preMax) * (index + 1)

        return ans


obj = Solution()
print(obj.countCommas(1004590))