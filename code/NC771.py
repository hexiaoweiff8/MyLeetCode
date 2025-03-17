class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jwlSet = set(jewels)
        ret = 0
        for stone in stones:
            if stone in jwlSet:
                ret += 1

        return ret


obj = Solution()
print(obj.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
print(obj.numJewelsInStones(jewels="z", stones="ZZ"))
