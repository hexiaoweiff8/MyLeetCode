class Solution(object):
    def maxmiumScore(self, cards, cnt):
        """
        :type cards: List[int]
        :type cnt: int
        :rtype: int
        """
        cards.sort(reverse=True)
        s = sum(cards[:cnt])
        if s % 2 == 0:
            return s

        def replace_sum(x):
            for v in cards[cnt:]:
                if v % 2 != x % 2:  # 找到一个最大的奇偶性和 x 不同的数
                    return s - x + v  # 用 v 替换 s
            return 0
        x = cards[cnt - 1]
        ret = replace_sum(x)
        for v in cards[cnt - 1:: -1]:
            if v % 2 != x % 2:
                ret = max(ret, replace_sum(v))
                break
        return ret

