import collections


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        count = collections.Counter(tasks)
        ans = 0
        for i in count:
            if count[i] == 1:
                return -1
            else:
                ans += (count[i] + 2) // 3
        return ans