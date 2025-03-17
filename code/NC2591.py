class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        money -= children
        if money < 0:
            return -1
        ret = min(money // 7, children)
        money -= ret * 7
        children -= ret
        if children == 0 and money or children == 1 and money == 3:
            ret -= 1
        return ret



obj = Solution()
# print(obj.distMoney(1, 2))
# print(obj.distMoney(2, 2))
# print(obj.distMoney(4, 2))
# print(obj.distMoney(25, 3))
# print(obj.distMoney(8, 2))
# print(obj.distMoney(16, 10))
print(obj.distMoney(9, 2))