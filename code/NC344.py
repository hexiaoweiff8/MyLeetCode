class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return s


obj = Solution()
print(obj.reverseString(["h", "e", "l", "l", "o"]))
print(obj.reverseString(["H", "a", "n", "n", "a", "h"]))
