class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        for index, val in enumerate(reward2):
            reward1[index] -= val
        reward1.sort(reverse=True)
        return sum(reward2) + sum(reward1[:k])