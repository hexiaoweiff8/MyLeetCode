class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomatoSlices % 2 == 1 or tomatoSlices < 2 * cheeseSlices or cheeseSlices * 4 < tomatoSlices:
            return []
        # 二分法判断两种数量
        # return [tomatoSlices // 2 - cheeseSlices, cheeseSlices * 2 - tomatoSlices // 2]
        left, right = 0, cheeseSlices
        while left <= right:
            mid = (left + right) // 2
            t = mid * 4 + (cheeseSlices - mid) * 2
            if t < tomatoSlices:
                left = mid + 1
            elif t > tomatoSlices:
                right = mid - 1
            else:
                return [mid, cheeseSlices - mid]