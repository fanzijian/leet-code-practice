class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        def is_target_restaurant(val):
            flag = True
            if veganFriendly and not val[2]:
                flag = False
            if val[3] > maxPrice or val[4] > maxDistance:
                flag = False
            return flag

        def cp(x, y):
            if x[1] == y[1]:
                return x[0] - y[0]
            return x[1] - y[1]

        restaurants = filter(is_target_restaurant, restaurants)
        # print restaurants
        restaurants.sort(cmp = cp, reverse=True)
        # print restaurants
        return [val[0] for val in restaurants]

a= Solution()
restaurants = [[1, 4, 1, 40, 10], [
    2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 8, 1, 15, 1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
print a.filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance)
