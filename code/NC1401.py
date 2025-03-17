class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        # 区分九个区域, 位于四角的位置只需要判断对应角到圆心距离判断是否相交
        # 中心区域全部相交
        # 上下左右四个区域判断勾股定理
        # 四角
        if xCenter < x1 and yCenter > y2:
            # 左上判断左上角到圆心距离是否大于半径
            disX, disY = x1 - xCenter, y2 - yCenter
            return disX * disX + disY * disY <= radius * radius
        elif xCenter < x1 and yCenter < y1:
            # 左下判断左下角到圆心距离是否大于半径
            disX, disY = x1 - xCenter, y1 - yCenter
            return disX * disX + disY * disY <= radius * radius
        elif xCenter > x2 and yCenter < y1:
            # 右下判断右下角到圆心距离是否大于半径
            disX, disY = x2 - xCenter, y1 - yCenter
            return disX * disX + disY * disY <= radius * radius
        elif xCenter > x2 and yCenter > y2:
            # 右上判断右上角到圆心距离是否大于半径
            disX, disY = x2 - xCenter, y2 - yCenter
            return disX * disX + disY * disY <= radius * radius
        elif x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            # 中心
            return True
        else:
            # 上下左右
            if yCenter > y2:
                # 上
                return radius >= yCenter - y2
            elif yCenter < y1:
                # 下
                return radius >= y1 - yCenter
            elif xCenter < x1:
                # 左
                return radius >= x1 - xCenter
            elif xCenter > x2:
                # 右
                return radius >= xCenter - x2
            else:
                return False


obj = Solution()
print(obj.checkOverlap(radius=1, xCenter=0, yCenter=0, x1=1, y1=-1, x2=3, y2=1))
print(obj.checkOverlap(radius=1, xCenter=1, yCenter=1, x1=1, y1=-3, x2=2, y2=-1))
print(obj.checkOverlap(radius=1, xCenter=0, yCenter=0, x1=-1, y1=0, x2=0, y2=1))
print(obj.checkOverlap(
    24,
    13,
    1,
    0,
    15,
    5,
    18))
