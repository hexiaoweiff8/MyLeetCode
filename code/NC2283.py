class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {}
        lenNum = len(num)
        for item in num:
            dict[int(item)] = dict.get(int(item), 0) + 1

        for index in range(lenNum):
            if int(num[index]) != dict.get(index, 0):
                return False

        return True


obj = Solution()
print(obj.digitCount('030'))

