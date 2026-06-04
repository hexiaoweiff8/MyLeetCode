class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        ans = 0
        for num in range(num1, num2 + 1):
            tmpNum = num
            preNum = -1
            prePreNum = -1
            # 判断是否为波峰/谷
            while tmpNum:
                oneNum = tmpNum % 10
                if preNum != -1 and prePreNum != -1:
                    if (preNum > prePreNum and oneNum < preNum) or (preNum < prePreNum and oneNum > preNum):
                        # 满足波峰/谷条件
                        ans += 1

                prePreNum = preNum
                preNum = oneNum
                tmpNum //= 10

        return ans