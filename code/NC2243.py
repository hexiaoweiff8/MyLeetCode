class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            new_s = ''
            for i in range(0, len(s), k):
                new_s += str(sum(map(int, list(s[i:i+k]))))
            s = new_s
        return s
