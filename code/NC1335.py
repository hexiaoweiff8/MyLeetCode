from itertools import accumulate


class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n = len(jobDifficulty)
        if n < d:
            return -1

        f = list(accumulate(jobDifficulty, max))
        for i in range(1, d):
            for j in range(n - 1, i - 1, -1):
                f[j] = 999999999
                mx = 0
                for k in range(j, i - 1, -1):
                    mx = max(mx, jobDifficulty[k])
                    f[j] = min(f[j], f[k - 1] + mx)
        return f[-1]


obj = Solution()
print(obj.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))