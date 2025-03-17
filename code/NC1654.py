class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        s = set(forbidden)
        q = [(0, 1)]
        vis = {(0, 1)}
        ret = 0
        while q:
            for _ in range(len(q)):
                i, k = q.pop(0)
                if i == x:
                    return ret
                nxt = [(i + a, 1)]
                if k & 1:
                    nxt.append((i - b, 0))
                for j, k in nxt:
                    if 0 <= j < 6000 and j not in s and (j, k) not in vis:
                        q.append((j, k))
                        vis.add((j, k))
            ret += 1
        return -1


obj = Solution()
print(obj.minimumJumps())