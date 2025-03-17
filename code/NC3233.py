class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        ans = r - l + 1
        for i in range(l, r+1):
            count = 1
            for j in [2, 3, 5, 7]:
                if i % j == 0 and i != j:
                    count += 1
            if count == 2:
                ans -= 1
        return ans
