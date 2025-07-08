from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        g = defaultdict(list)
        l, r = 9999999, 0
        for s, e in events:
            g[s].append(e)
            l = min(l, s)
            r = max(r, e)
        pq = []
        ans = 0
        for i in range(l, r + 1):
            while pq and pq[0] < i:
                heappop(pq)
            for e in g[i]:
                heappush(pq, e)
            if pq:
                heappop(pq)
                ans += 1
        return ans