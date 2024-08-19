from enum import Enum
from heapq import *


class Direction(Enum):
    UP = 1
    DOWN = 2
    IDLE = 3


class Location(Enum):
    INSIDE_ELEVATOR = 1
    OUTSIDE_ELEVATOR = 2


class Request:
    def __init__(self, currFloor: int, destinationFloor: int, direction: Direction, location: Location):
        self.currFloor = currFloor
        self.destinationFloor = destinationFloor
        self.direction = direction
        self.location = location

    # used in heapq comparison
    def __lt__(self, other) -> bool:
        if self.direction == Direction.UP:
            return self.destinationFloor <= other.destinationFloor
        else:
            return self.destinationFloor > other.destinationFloor


# Idea from: https://tedweishiwang.github.io/journal/object-oriented-design-elevator.html
class Elevator:
    def __init__(self, currFloor: int):
        self.currFloor = currFloor
        self.direction = Direction.IDLE
        self.upQueue = []
        heapify(self.upQueue)
        self.downQueue = []
        heapify(self.downQueue)

    def sendUpRequest(self, upRequest: Request):
        if upRequest.location == Location.OUTSIDE_ELEVATOR:
            # need to pick up the person out side of the elevator
            heappush(self.upQueue, Request(upRequest.currFloor, upRequest.currFloor, Direction.UP, Location.OUTSIDE_ELEVATOR))
            print("Append upRequest going to floor " + str(upRequest.currFloor))

        heappush(self.upQueue, upRequest)
        print("Append upRequest going to floor " + str(upRequest.destinationFloor))

    def sendDownRequest(self, downRequest: Request):
        if downRequest.location == Location.OUTSIDE_ELEVATOR:
            heappush(self.downQueue, Request(downRequest.currFloor, downRequest.currFloor, Direction.DOWN, Location.OUTSIDE_ELEVATOR))
            print("Append downRequest going to floor " + str(downRequest.currFloor))

        heappush(self.downQueue, downRequest)
        print("Append downRequest going to floor " + str(downRequest.destinationFloor))

    def processUpRequest(self):
        while self.upQueue:
            upRequest = heappop(self.upQueue)
            # communicate with the hardware to move to that floor
            self.currFloor = upRequest.destinationFloor
            print("Processing upRequests. Elevator stopped at floor " + str(self.currFloor))

        if self.downQueue:
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.IDLE

    def processDownRequest(self):
        while self.downQueue:
            downRequest = heappop(self.downQueue)
            # communicate with the hardware to move to that floor
            self.currFloor = downRequest.destinationFloor
            print("Processing downRequests. Elevator stopped at floor " + str(self.currFloor))

        if self.upQueue:
            self.direction = Direction.UP
        else:
            self.direction = Direction.IDLE

    def processRequest(self):
        if self.direction == Direction.UP or self.direction == Direction.IDLE:
            self.processUpRequest()
            self.processDownRequest()
        else:
            self.processDownRequest()
            self.processUpRequest()

    def run(self):
        while len(self.upQueue) > 0 or len(self.downQueue) > 0:
            self.processRequest()

        print("Finished all requests!")
        self.direction = Direction.IDLE


elevator = Elevator(0)
upRequest1 = Request(elevator.currFloor, 5, Direction.UP, Location.INSIDE_ELEVATOR)
upRequest2 = Request(elevator.currFloor, 3, Direction.UP, Location.INSIDE_ELEVATOR)

downRequest1 = Request(elevator.currFloor, 1, Direction.DOWN, Location.INSIDE_ELEVATOR)
downRequest2 = Request(elevator.currFloor, 2, Direction.DOWN, Location.INSIDE_ELEVATOR)
downRequest3 = Request(4, 0, Direction.DOWN, Location.OUTSIDE_ELEVATOR)

# Two people inside the elevator pressed button to go up to floor 5 and 3.
elevator.sendUpRequest(upRequest1)
elevator.sendUpRequest(upRequest2)

# One people outside the elevator at floor 4 pressed button to go down to floor 0
elevator.sendDownRequest(downRequest3)

# Two people inside the elevator pressed button to go down to floor 1 and 2.
elevator.sendDownRequest(downRequest1)
elevator.sendDownRequest(downRequest2)

elevator.run()
