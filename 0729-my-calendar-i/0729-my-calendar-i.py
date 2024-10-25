class MyCalendar:

    def __init__(self):
        self._bookings = []

    def can_book(self, event):
        def overlapped(event1, event2):
            return event1[1] > event2[0] and event2[1] > event1[0]
        
        location = bisect.bisect_left(self._bookings, event)
        
        if not self._bookings:
            return True, location 
        
        if location < len(self._bookings) and overlapped(self._bookings[location], event):
            return False, None
        
        if location > 0 and overlapped(self._bookings[location-1], event):
            return False, None
            
        return True, location

    def book(self, start: int, end: int) -> bool:
        event = (start, end)
        can, location = self.can_book(event)
        print(location)
        if can:
            self._bookings.insert(location, event)
            return True
        
        return False