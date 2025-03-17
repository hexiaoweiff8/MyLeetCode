class Solution(object):
    def findMaximumElegance(self, items, k):
        """
        :type items: List[List[int]]
        :type k: int
        :rtype: int
        """
        items.sort(key=lambda x: (x[0], x[1]))
        dp = [0] * k
        for item in items:
            i, j = item
            if i > 1 and dp[-1] < j:
                dp[-1] = j
            else:
                dp.append(j)
            k -= 1
            if k == 0:
                break
        return sum(dp)