class Solution(object):
    def maxStudents(self, seats):
        """
        :type seats: List[List[str]]
        :rtype: int
        """
        n = len(seats)
        m = len(seats[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

