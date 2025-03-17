class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        m = len(colsum)
        n = sum(colsum)
        if n != upper + lower:
            return []
        res = [[0] * m for _ in range(2)]
        for i in range(m):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
                upper -= 1
                lower -= 1
        for i in range(m):
            if colsum[i] == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
        return res if upper == 0 and lower == 0 else []