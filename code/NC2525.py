class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        isBulkey = isHeavy = False
        if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000:
            isBulkey = True
        if mass >= 100:
            isHeavy = True

        if isBulkey and isHeavy:
            return "Both"
        elif isBulkey:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        else:
            return "Neither"


