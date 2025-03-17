class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        l, r = 0, k
        ans = 0
        while r <= len(str(num)):
            if int(str(num)[l:r]) != 0 and num % int(str(num)[l:r]) == 0:
                ans += 1
            l += 1
            r += 1
        return ans