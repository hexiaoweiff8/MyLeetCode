class Solution(object):
    def minEnd(self, n, x):
        n -= 1
        i = j = 0
        while n >> j:
            if (x >> i & 1) == 0:
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x


obj = Solution()
print(obj.minEnd(2, 7))