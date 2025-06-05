class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        p = list(range(26))
        ans = ""
        for a, b in zip(s1, s2):
            x, y = find(ord(a) - ord('a')), find(ord(b) - ord('a'))
            if x < y:
                p[y] = x
            else:
                p[x] = y
        return "".join(chr(find(ord(c) - ord('a')) + ord('a')) for c in baseStr)


obj = Solution()
print(obj.smallestEquivalentString(s1="leetcode", s2="programs", baseStr="sourcecode"))
