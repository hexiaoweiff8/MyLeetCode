class Solution(object):
    def relocateMarbles(self, nums, moveFrom, moveTo):
        """
        :type nums: List[int]
        :type moveFrom: List[int]
        :type moveTo: List[int]
        :rtype: List[int]
        """
        posDic = {}
        for i in nums:
            posDic[i] = True

        for i in range(len(moveFrom)):
            if moveFrom[i] in posDic:
                del posDic[moveFrom[i]]
            posDic[moveTo[i]] = True

        return sorted(posDic.keys())


obj = Solution()
print(obj.relocateMarbles([1,1,3,3],[1,3],[2,2]))