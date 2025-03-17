from functools import lru_cache


class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """
        mx = 0
        prev = [[] for _ in range(n + 1)]
        for x, y in relations:
            prev[y].append(x)

        @lru_cache(None)
        def dp(i):
            cur = 0
            for p in prev[i]:
                cur = max(cur, dp(p))
            cur += time[i - 1]
            return cur

        for i in range(1, n + 1):
            mx = max(mx, dp(i))
        return mx


obj = Solution()
# print(obj.minimumTime(n=5, relations=[[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], time=[1, 2, 3, 4, 5]))
print(obj.minimumTime(n=2, relations=[[2, 1]], time=[10000, 10000]))
