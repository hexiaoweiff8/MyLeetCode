from itertools import combinations


class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        def f(a, mx):
            a += [1, mx]
            a.sort()
            return set(y - x for x, y in combinations(a, 2))

        h_set = f(hFences, m)
        v_set = f(vFences, n)
        ans = max(h_set & v_set, default=0)
        return ans * ans % (10 ** 9 + 7) if ans else -1