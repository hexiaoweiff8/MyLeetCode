class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)


