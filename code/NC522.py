class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        ans = -1
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j:
                    k, w = 0, 0
                    while k < len(s) and w < len(t):
                        if s[k] == t[w]:
                            k += 1
                        w += 1
                    if k == 0 or k == len(s):
                        break
                    else:
                        ans = max(ans, len(s))
        return ans

obj = Solution()
print(obj.findLUSlength(["aaa", "aaa", "aa"]))
print(obj.findLUSlength(["a","b","c","d","e","f","a","b","c","d","e","f"]))

