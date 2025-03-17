from collections import defaultdict

from sortedcontainers import SortedList


class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.food_map = {}
        self.food_cuisine_map = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            self.food_cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        old_rating, cuisine = self.food_map[food]
        sortedList = self.food_cuisine_map[cuisine]
        sortedList.remove((-old_rating, food))
        sortedList.add((-newRating, food))
        self.food_map[food][0] = newRating

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.food_cuisine_map[cuisine][0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)