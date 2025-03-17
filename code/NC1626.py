class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        memberCount = len(scores)
        dp = [0] * memberCount
        ret = 0
        for index in range(memberCount):
            score = scores[index]
            age = ages[index]
            for index2 in range(index):
                if age >= ages[index2]:
                    dp[index] = max(dp[index], dp[index2])
            dp[index] += score
            ret = max(ret, dp[index])
        return ret


obj = Solution()
print(obj.bestTeamScore([1, 3, 5, 10, 15], [1, 2, 3, 4, 5]))
