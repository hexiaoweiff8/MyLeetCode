class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + mat[i - 1][j - 1]

        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(min(i, j), 0, -1):
                    if s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k] <= threshold:
                        ans = max(ans, k)
                        break
        return ans
