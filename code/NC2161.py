class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        lList, pList = [] , []
        sameCount = 0
        for i in nums:
            if i < pivot:
                lList.append(i)
            elif i > pivot:
                pList.append(i)
            else:
                sameCount += 1
        return lList + [pivot] * sameCount + pList