class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        n += 1
        while True:
            y = n
            cnt = [0] * 10
            while y:
                cnt[y % 10] += 1
                y //= 10
            if all(cnt[i] == i for i in range(10) if cnt[i]):
                return n
            n += 1
