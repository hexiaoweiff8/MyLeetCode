class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        maxGap = gap = 0
        isSingle = True
        for seat in seats:
            if seat == 0:
                gap += 1
            else:
                if gap > maxGap:
                    maxGap = gap * (2 if isSingle else 1)
                gap = 0
                isSingle = False
        if seats[len(seats) - 1] == 0:
            gap *= 2
        if gap > maxGap:
            maxGap = gap

        return (maxGap + 1) // 2


obj = Solution()
print(obj.maxDistToClosest(seats = [1,0,0,0,1,0,1]))
print(obj.maxDistToClosest(seats = [1,0,0,0]))