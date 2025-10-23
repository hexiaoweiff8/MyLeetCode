class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_array = [int(item) for item in s]
        s_tmp = []
        while len(s_array) > 2:
            for i in range(len(s_array) - 1):
                s_tmp.append((s_array[i] + s_array[i + 1]) % 10)
            s_array = s_tmp
            s_tmp = []

        return s_array[0] == s_array[1]


obj = Solution()
print(obj.hasSameDigits("3902"))