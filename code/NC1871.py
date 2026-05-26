class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        df = [False] * n
        sum_ = [0] * (n + 1)
        df[0] = True
        sum_[1] = 1
        for i in range(1, n):
            df[i] = i >= minJump and s[i] == '0' and sum_[i - minJump + 1] > sum_[max(i - maxJump, 0)]
            sum_[i + 1] = sum_[i] + df[i]
        return df[-1]

