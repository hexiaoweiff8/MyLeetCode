import collections


class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        # 最大奇数
        max_odd = max(counter[i] for i in counter if counter[i] % 2)
        # 最小偶数
        min_even = min(counter[i] for i in counter if not counter[i] % 2)
        # 返回 奇数与偶数之间最大的差值
        return max_odd - min_even