class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        sList = list(s)
        count = 0
        sameCount = 1
        i = 1
        while i < n:
            if sList[i] != sList[i - 1]:
                if sameCount % 2:
                    count += 1
                    sList[i] = sList[i - 1]
                    i += 1
                sameCount = 1
            else:
                sameCount += 1
            i += 1
        return count


obj = Solution()
print(obj.minChanges("11000111"))

