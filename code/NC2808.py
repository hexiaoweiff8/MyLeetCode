class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ret = n = len(nums)
        for lst in pos.values():
            lst.append(lst[0] + n)
            mx = max(j - i for i, j in pairwise(lst))
            ret = min(mx, ret)
        return ret // 2
