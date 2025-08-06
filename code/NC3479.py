class SegmentTree:
    def __init__(self, a):
        n = len(a)
        self.max = [0] * (2 << (n - 1).bit_length())
        self.build(a, 1, 0, n - 1)

    def build(self, a, node, start, end):
        if start == end:
            self.max[node] = a[start]
            return
        mid = (start + end) // 2
        self.build(a, node * 2, start, mid)
        self.build(a, node * 2 + 1, mid + 1, end)
        self.maintain(node)

    def maintain(self, node):
        self.max[node] = max(self.max[node * 2], self.max[node * 2 + 1])

    def find_first_and_update(self, node, start, end, val):
        if self.max[node] < val:
            return -1
        if start == end:
            self.max[node] = -1
            return start
        m = (start + end) // 2
        i = self.find_first_and_update(node * 2, start, m, val)
        if i == -1:
            i = self.find_first_and_update(node * 2 + 1, m + 1, end, val)
        self.maintain(node)
        return i


class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        t = SegmentTree(baskets)
        n = len(fruits)
        ans = 0
        for i in range(n):
            j = t.find_first_and_update(1, 0, n - 1, fruits[i])
            if j == -1:
                ans += 1
        return ans
