from entities.user import User
from entities.restaurant import Restaurant
from entities.timeslot import TimeSlot
from services.restaurant_registry import RestaurantRegistry
from datetime import datetime, timedelta

# Example usage:

# Create instances of entities
restaurant_registry = RestaurantRegistry()
restaurant1 = Restaurant("Restaurant A", "Location A", ["Cuisine A", "Cuisine B"], 4, True, 3)  # Update max_days_future to 3
restaurant2 = Restaurant("Restaurant B", "Location B", ["Cuisine C", "Cuisine D"], 5, False, 3)  # Update max_days_future to 3
restaurant_registry.register_restaurant(restaurant1)
restaurant_registry.register_restaurant(restaurant2)

user = User(1, "User A")
user.login()

# Search for restaurants with a minimum rating of 4 and serving vegetarian food
search_results = restaurant_registry.search_restaurants("Location", min_rating=4, is_veg=True)
print("Search Results:")
for restaurant in search_results:
    print(restaurant.name)

# Add slots for booking
time_slot1 = TimeSlot(1, datetime.now() + timedelta(hours=1))
time_slot2 = TimeSlot(2, datetime.now() + timedelta(hours=3))  
restaurant1.add_slot(time_slot1)
restaurant1.add_slot(time_slot2)

# Check if the entered slot is within max_days_future days
def is_within_max_days(slot):
    return restaurant1.is_within_max_days(slot.start_time)

# Book a table at the restaurant
slot_id = 1  # Example slot ID
if is_within_max_days(time_slot1):
    booking_status = restaurant1.book(user, slot_id, 4)  # Example: booking for slot 1 for 4 people
    print("\nBooking status:", booking_status)
else:
    print("The selected slot is greater than {} days in the future. Please select a different slot.".format(restaurant1.max_days_future))
