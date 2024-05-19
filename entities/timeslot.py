from datetime import timedelta

class TimeSlot:
    def __init__(self, slot_id, start_time):
        self.slot_id = slot_id
        self.start_time = start_time
        self.end_time = (start_time + timedelta(hours=1)).strftime("%I:%M %p")
