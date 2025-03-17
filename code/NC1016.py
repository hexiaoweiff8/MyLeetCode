class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        # return all(bin(i)[2:] in s for i in range(1, n + 1))
        seen = set()
        s = list(map(int, s))
        for i, x in enumerate(s):
            if x == 0:
                continue
            j = i + 1
            while x <= n:
                seen.add(x)
                if j == len(s):
                    break
                x = (x << 1) | s[j]
                j += 1
        return len(seen) == n

