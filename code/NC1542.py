from collections import defaultdict


class Solution(object):
    def longestAwesome(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                pass
        # sCount = Counter(s)
        # singleCount = 0
        # for count in sCount:
        #     if sCount[count] % 2 == 1:
        #         singleCount += 1
        #
        # return len(s) - singleCount + (1 if singleCount > 0 else 0)


obj = Solution()
# print(obj.longestAwesome("3242415"))
# print(obj.longestAwesome("12345678"))
print(obj.longestAwesome("9498331"))