class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        count1, count2 = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                count1 += int(num[i])
            else:
                count2 += int(num[i])
        return count1 == count2