class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        numList = [char for char in str(num) if char != "0"]
        numList.sort()
        numStr1, numStr2 = "", ""
        for index, char in enumerate(numList):
            if index % 2 == 0:
                numStr1 += char
            else:
                numStr2 += char
        return (int(numStr1) if numStr1 else 0) + (int(numStr2) if numStr2 else 0)


obj = Solution()
print(obj.splitNum(321))
print(obj.splitNum(4325))
print(obj.splitNum(687))
print(obj.splitNum(10))

