from collections import Counter


class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        dic = Counter()
        ans = 0
        maxCount = 0
        for i in range(1, n + 1):
            s = 0
            for j in str(i):
                s += int(j)
            dic[s] += 1
            if dic[s] > maxCount:
                maxCount = dic[s]
                ans = 1
            elif dic[s] == maxCount:
                ans += 1
        return ans


obj = Solution()
print(obj.countLargestGroup(n=13))