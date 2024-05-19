class RestaurantRegistry:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.restaurants = []

    def register_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def search_restaurants(self, query, min_rating=None, is_veg=None):
        matches = []
        for restaurant in self.restaurants:
            if restaurant.matches_search_criteria(query, min_rating, is_veg):
                matches.append(restaurant)
        return matches
