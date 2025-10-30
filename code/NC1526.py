class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        pre = target[0]
        res = pre
        for i in range(1, len(target)):
            if target[i] > pre:
                res += target[i] - pre
            pre = target[i]
        return res
