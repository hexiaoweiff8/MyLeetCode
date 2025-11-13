class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = list(s)
        ans = 0
        index = zeroLen = 0
        oneStack = []
        while index < len(sList):
            if sList[index] == '1':
                if zeroLen > 0:
                    ans += len(oneStack)
                    zeroLen = 0
                oneStack.append(index)
                index += 1
            else:
                zeroLen += 1
                index += 1
        if zeroLen > 0:
            ans += len(oneStack)
        return ans


obj = Solution()
# print(obj.maxOperations("1001101"))
print(obj.maxOperations("110"))
