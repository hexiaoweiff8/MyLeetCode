class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        pre, prePre = colors[-1], colors[-2]
        ans = 0
        for i in range(len(colors)):
            if pre != prePre and pre != colors[i]:
                ans += 1
            prePre = pre
            pre = colors[i]
        return ans