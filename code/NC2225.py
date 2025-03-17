class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        win = {}
        lose = {}
        ret = [[], []]
        for match in matches:
            win[match[0]] = win.get(match[0], 0) + 1
            lose[match[1]] = lose.get(match[1], 0) + 1
        for winner, _ in win.items():
            if lose.get(winner, 0) == 0:
                ret[0].append(winner)
        for loser, count in lose.items():
            if count == 1:
                ret[1].append(loser)
        ret[0].sort()
        ret[1].sort()
        return ret