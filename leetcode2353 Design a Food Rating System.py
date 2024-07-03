from typing import List
from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineToSortedList = {}
        self.foodToRating = {}
        self.foodToCuisine = {}

        n = len(foods)
        for i in range(n):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.foodToRating[food] = rating
            self.foodToCuisine[food] = cuisine

            if cuisine not in self.cuisineToSortedList:
                self.cuisineToSortedList[cuisine] = SortedList()
            self.cuisineToSortedList[cuisine].add([-rating, food])

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.foodToRating[food]
        cuisine = self.foodToCuisine[food]
        self.cuisineToSortedList[cuisine].remove([-oldRating, food])

        self.foodToRating[food] = newRating
        self.cuisineToSortedList[cuisine].add([-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        highestRating, food = self.cuisineToSortedList[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
