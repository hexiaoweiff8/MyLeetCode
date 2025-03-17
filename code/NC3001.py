class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """

        aSubn = a - e
        bSubn = b - f
        cSubn = c - e
        dSubn = d - f
        aSub = abs(aSubn)
        bSub = abs(bSubn)
        cSub = abs(cSubn)
        dSub = abs(dSubn)
        # 先处理a/b步数
        ans = 0
        # 纵向坐标相同
        if aSub == 0:
            # 判断cd是否遮挡ab 判断a与c是都都在e的同一侧
            if cSub == 0 and bSub > dSub and ((bSubn < 0 and dSubn < 0) or (bSubn > 0 and dSubn > 0)):
                ans = 2
            else:
                ans = 1
        elif bSub == 0:
            # 横向坐标相同
            # 判断cd是否遮挡ab 判断a与c是都都在e的同一侧
            if dSub == 0 and aSub > cSub and ((aSubn < 0 and cSubn < 0) or (aSubn > 0 and cSubn > 0)):
                ans = 2
            else:
                ans = 1
        else:
            ans = 2

        # 判断是否同一条线
        if cSub == dSub:
            # 判断ab是否遮挡 判断ab和cd是否在同一侧
            if aSub == bSub and aSub < cSub and (((aSubn < 0 and bSubn < 0) and (cSubn < 0 and dSubn < 0))
                                                 or ((aSubn > 0 and bSubn > 0) and (cSubn > 0 and dSubn > 0))
                                                 or ((aSubn < 0 < bSubn) and (cSubn < 0 < dSubn))
                                                 or ((aSubn > 0 > bSubn) and (cSubn > 0 > dSubn))):
                ans = min(ans, 2)
            else:
                ans = min(ans, 1)

        return ans


obj = Solution()
print(obj.minMovesToCaptureTheQueen(1, 1, 1, 4, 1, 8))