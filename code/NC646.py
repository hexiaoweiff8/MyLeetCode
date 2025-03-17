class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # pairs.sort(key=lambda x: x[1])
        # cur = -float('inf')
        # res = 0
        # for pair in pairs:
        #     if pair[0] > cur:
        #         res += 1
        #         cur = pair[1]
        # return res
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]