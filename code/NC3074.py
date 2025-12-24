class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """

        capacity.sort(reverse=True)
        index = 0
        count = 1
        for appleCount in apple:
            while appleCount > 0 and index < len(capacity):
                if capacity[index] >= appleCount:
                    capacity[index] -= appleCount
                    appleCount = 0
                else:
                    appleCount -= capacity[index]
                    capacity[index] = 0
                    index += 1
                    count += 1

        return count


obj = Solution()
# print(obj.minimumBoxes([1,2,3], [4,3,1,5,2]))
print(obj.minimumBoxes([5,5,5], [2,4,2,7]))