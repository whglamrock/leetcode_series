from collections import deque
from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        waitingPassengers = deque(passengers)

        arrivalTimesCanCatch = set()
        isLastBusFull = False
        for i, busArrival in enumerate(buses):
            numOfPeopleGetOnBus = 0
            for _ in range(capacity):
                if waitingPassengers and waitingPassengers[0] <= busArrival:
                    arrivalTimesCanCatch.add(waitingPassengers.popleft())
                    numOfPeopleGetOnBus += 1
                else:
                    break
            if i == len(buses) - 1:
                isLastBusFull = numOfPeopleGetOnBus == capacity

        # 1) if nobody can catch bus it means all of them arrive too late
        numOfPassengersCanCatchBus = len(passengers) - len(waitingPassengers)
        if numOfPassengersCanCatchBus == 0:
            return buses[-1]

        # 2) if the last passenger arrives before the last bus arrival and the last bus is not full
        arrivalTimeOfLastPassenger = passengers[numOfPassengersCanCatchBus - 1]
        if not isLastBusFull and buses[-1] != arrivalTimeOfLastPassenger:
            return buses[-1]

        # 3) regular case. We just need to take someone else's spot
        for time in range(arrivalTimeOfLastPassenger - 1, 0, -1):
            if time not in arrivalTimesCanCatch:
                return time
        return -1
