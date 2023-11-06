class SeatManager:

    def __init__(self, n: int):
        self.seats=[]
        for i in range(n):
                heappush(self.seats,i+1)
        
    def reserve(self) -> int:
            return heappop(self.seats)

    def unreserve(self, seatNumber: int) -> None:
            heappush(self.seats,seatNumber)
            return

        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)