class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        preChar = s[0]
        sameChar = 1
        ans = [s[0]]
        for i in range(1, len(s)):
            if s[i] == preChar:
                if sameChar + 1 < 3:
                    ans.append(s[i])
                    sameChar += 1
            else:
                sameChar = 1
                ans.append(s[i])
                preChar = s[i]
        return ''.join(ans)