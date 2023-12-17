class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating={}
        self.cuisines=defaultdict(list)
        self.foodCuisine={}
        for i in range(len(foods)):
            self.rating[foods[i]]=-ratings[i]
            self.foodCuisine[foods[i]]=cuisines[i]
            heapq.heappush(self.cuisines[cuisines[i]],(-ratings[i],foods[i]))
    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food]=-newRating
        cuisine=self.foodCuisine[food]
        heapq.heappush(self.cuisines[cuisine],(-newRating,food))
    def highestRated(self, cuisine: str) -> str:
        while self.rating[self.cuisines[cuisine][0][1]] !=self.cuisines[cuisine][0][0]:
           heapq.heappop(self.cuisines[cuisine])
        return self.cuisines[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)