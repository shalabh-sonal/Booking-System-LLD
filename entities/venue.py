from abc import ABC, abstractmethod
import threading


class Venue(ABC):
    def __init__(self, name, location, category, rating, max_days_future):
        self.name = name
        self.location = location
        self.category = category
        self.rating = rating
        self.max_days_future = max_days_future
        self.slots = {}
        self.bookings = {}
        self.lock = threading.Lock()  # Lock for synchronization

    def add_slot(self, slot):
        with self.lock:
            self.slots[slot.slot_id] = slot

    def book(self, user, slot_id, num_people):
        if not user.is_authenticated:
            print("User is not authenticated.")
            return False

        if not self.is_within_max_days(self.slots[slot_id].start_time):
            print("Booking can only be made up to {} days in advance.".format(self.max_days_future))
            return False

        with self.lock:  # Acquire lock before modifying bookings
            if self.is_slot_available(slot_id):
                self.bookings[slot_id] = num_people
                return True
            else:
                return False

    @abstractmethod
    def is_slot_available(self, slot_id):
        pass

    @abstractmethod
    def is_within_max_days(self, slot_date):
        pass

    @abstractmethod
    def matches_search_criteria(self, query, min_rating=None, is_veg=None):
        pass
