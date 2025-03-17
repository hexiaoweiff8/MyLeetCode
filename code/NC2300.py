class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        potionsLen = len(potions)
        res = []
        for i, spell in enumerate(spells):
            hasVal = False
            # 二分法
            left = 0
            right = potionsLen - 1
            mid = None
            while left < right:
                mid = (left + right) // 2
                if potions[mid] * spell < success:
                    left = mid + 1
                else:
                    right = mid
            if potions[left] * spell >= success:
                res.append(potionsLen - left)
                hasVal = True
            if not hasVal:
                res.append(0)
        return res


obj = Solution()
print(obj.successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
