from entities.venue import Venue
from datetime import datetime, timedelta

class Restaurant(Venue):
    def __init__(self, name, location, cuisines, rating, veg, max_days_future):
        super().__init__(name, location, "Restaurant", rating, max_days_future)
        self.cuisines = cuisines
        self.veg = veg

    def is_slot_available(self, slot_id):
        return slot_id in self.slots and slot_id not in self.bookings

    def is_within_max_days(self, slot_date):
        max_booking_date = datetime.now().date() + timedelta(days=self.max_days_future)
        return slot_date.date() <= max_booking_date

    def matches_search_criteria(self, query, min_rating=None, is_veg=None):
        matches_criteria = query.lower() in self.name.lower() or \
                           query.lower() in self.location.lower() or \
                           any(cuisine.lower() in query.lower() for cuisine in self.cuisines)

        if min_rating is not None:
            matches_criteria &= self.rating >= min_rating

        if is_veg is not None:
            matches_criteria &= self.veg == is_veg

        return matches_criteria
