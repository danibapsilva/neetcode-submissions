class MyCalendar:
    
    def __init__(self):
        self.bookings = [] # heap (start, end)

    def book(self, startTime: int, endTime: int) -> bool:
        for booking in self.bookings:
            if (
                startTime < booking[1] and endTime > booking[0]
            ):
                return False

        heapq.heappush(self.bookings, (startTime, endTime))
        return True        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)