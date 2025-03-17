class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * num_people
        index = 0
        while candies > 0:
            for i in range(num_people):
                if candies >= index + (i + 1):
                    res[i] += index + (i + 1)
                    candies -= index + (i + 1)
                else:
                    res[i] += candies
                    candies = 0
                    break
            index += num_people
        return res


obj = Solution()
print(obj.distributeCandies(10, 3))