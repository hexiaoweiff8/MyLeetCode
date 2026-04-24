class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        cnt_r = moves.count('R')
        cnt_l = moves.count('L')
        cnt = moves.count('_')
        return max(cnt_r, cnt_l) + cnt - min(cnt_r, cnt_l)
