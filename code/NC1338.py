import collections


class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = collections.Counter(arr)
        cnt = sorted(cnt.values(), reverse=True)
        ans, s, n = 0, 0, len(arr) // 2
        for x in cnt:
            s += x
            ans += 1
            if s >= n:
                break
        return ans
