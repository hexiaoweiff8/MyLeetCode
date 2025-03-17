class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """

        ret = []
        for left, right in zip(l, r):
            subNums = nums[left: right + 1]
            minVal = min(subNums)
            maxVal = max(subNums)
            if minVal == maxVal:
                ret.append(True)
                continue

            if (maxVal - minVal) % (right - left) != 0:
                ret.append(False)
                continue

            dis = (maxVal - minVal) // (right - left)
            flag = True
            itemSet = set()
            for index in range(left, right + 1):
                if (nums[index] - minVal) % dis != 0:
                    flag = False
                    break
                t = (nums[index] - minVal) // dis
                if t in itemSet:
                    flag = False
                    break
                itemSet.add(t)
            ret.append(flag)
        #     for index in range(len(l)):
        #         leftIndex = l[index]
        #         rightIndex = r[index]
        #         itemList = SortedList(nums[leftIndex: rightIndex + 1])
        #         ret.append(self.check(itemList))
        #         itemList.clear()
        #
        return ret
    #
    # def check(self, list):
    #     preSub = None
    #     for index in range(1, len(list)):
    #         sub = list[index - 1] - list[index]
    #         if preSub is not None and sub != preSub:
    #             return False
    #
    #         preSub = sub
    #     return True


obj = Solution()
print(obj.checkArithmeticSubarrays([4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]))
