class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        ans = 0
        for i in range(low, high + 1):
            numStr = str(i)
            if len(numStr) % 2 == 0 and sum(map(ord, numStr[:(len(numStr) // 2)])) == sum(map(ord, numStr[(len(numStr) // 2):])):
                ans += 1

        return ans
