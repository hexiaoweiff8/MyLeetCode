class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        f = [envelopes[0][1]]
        for i in range(1, n):
            if envelopes[i][1] > f[-1]:
                f.append(envelopes[i][1])
            else:
                l, r = 0, len(f) - 1
                while l < r:
                    mid = (l + r) >> 1
                    if f[mid] < envelopes[i][1]:
                        l = mid + 1
                    else:
                        r = mid
                f[l]= envelopes[i][1]
        return len(f)