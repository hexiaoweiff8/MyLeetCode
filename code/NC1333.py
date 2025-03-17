class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        ret = []
        for restaurant in restaurants:
            if veganFriendly == 1 and veganFriendly != restaurant[2]:
                continue
            if maxPrice < restaurant[3]:
                continue
            if maxDistance < restaurant[4]:
                continue
            ret.append(restaurant)
        ret.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [x[0] for x in ret]


obj = Solution()
print(obj.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=1, maxPrice=50, maxDistance=10))
print(obj.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=0, maxPrice=50, maxDistance=10))
print(obj.filterRestaurants(
    restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
    veganFriendly=0, maxPrice=30, maxDistance=3))
