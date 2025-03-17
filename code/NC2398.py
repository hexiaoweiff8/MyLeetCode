class Solution(object):
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        """
        :type chargeTimes: List[int]
        :type runningCosts: List[int]
        :type budget: int
        :rtype: int
        """
        q = []
        ret = s = l = 0
        for r, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            s += c
            while q and chargeTimes[q[-1]] <= t:
                q.pop()
            q.append(r)
            while q and (r - l + 1) * s + chargeTimes[q[0]] > budget:
                if q[0] == l:
                    q.pop(0)
                s -= runningCosts[l]
                l += 1
            ret = max(ret, r - l + 1)
        return ret