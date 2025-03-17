def testDy(p):
    dp = [0] * len(p)
    for index, val in enumerate(p):
        q = -1
        for index2 in range(index + 1):
            q = max(q, p[index2 - 1] + dp[index - index2])
        dp[index] = q
    return dp[-1]


