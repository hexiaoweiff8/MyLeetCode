class Solution(object):
    def canReachCorner(self, xCorner, yCorner, circles):
        """
        :type xCorner: int
        :type yCorner: int
        :type circles: List[List[int]]
        :rtype: bool
        """
        def in_cycle(ox, oy, r, x, y):
            return (ox - x) ** 2 + (oy - y) ** 2 <= r ** 2

        vis = [False] * len(circles)
        def dfs(i):
            x1, y1, r1 = circles[i]
            if y1 <= yCorner and abs(x1 - xCorner) <= r1 or\
                    x1 <= xCorner and y1 <= r1 or\
                    x1 > xCorner and in_cycle(x1, y1, r1, xCorner, 0):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if not vis[j] and\
                        (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2 and\
                        x1 * r2 + x2 * r1 < (r1 + r2) * xCorner and\
                        y1 * r2 + y2 * r1 < (r1 + r2) * yCorner and\
                        dfs(j):
                    return True
            return False

        for i, (x, y, r) in enumerate(circles):
            if in_cycle(x, y, r, 0, 0) or\
                in_cycle(x, y, r, xCorner, yCorner) or\
                not vis[i] and (x <= xCorner and abs(y - yCorner) <= r or
                                y <= yCorner and x <= r or
                                y > yCorner and in_cycle(x, y, r, 0, yCorner)) and dfs(i):
                return False
        return True