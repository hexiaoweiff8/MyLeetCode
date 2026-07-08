mod = 1000000007
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % mod

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        sum = [0] * (n + 1)
        x = [0] * (n + 1)
        cnt = [0] * (n + 1)
        for i in range(n):
            d = int(s[i])
            sum[i + 1] = sum[i] + d
            x[i + 1] = (x[i] * 10 + d) % mod if d > 0 else x[i]
            cnt[i + 1] = cnt[i] + (d > 0)

        m = len(queries)
        res = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = cnt[r] - cnt[l]
            res[i] = (x[r] - x[l] * pow10[length]) * (sum[r] - sum[l]) % mod

        return res


obj = Solution()
print(obj.sumAndMultiply(s="10203004", queries=[[0, 7], [1, 3], [4, 6]]))
