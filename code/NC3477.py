class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    del baskets[j]
                    ans += 1
                    break

        return len(fruits) - ans

obj = Solution()
# print(obj.numOfUnplacedFruits(fruits=
#                               [1, 4],
#                               baskets=
#                               [8, 1]))
# print(obj.numOfUnplacedFruits(fruits=
#                               [4, 2, 5],
#                               baskets=
#                               [3, 5, 4]))
# print(obj.numOfUnplacedFruits(fruits=
#                               [3, 6, 1],
#                               baskets=
#                               [6, 4, 7]))
# print(obj.numOfUnplacedFruits(fruits=
#                               [6, 5],
#                               baskets=
#                               [3, 5]))
print(obj.numOfUnplacedFruits(fruits=
                              [44, 10],
                              baskets=
                              [26, 5]))
