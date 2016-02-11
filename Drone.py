from enum import Enum

class Status(Enum):
    WAIT = 1
    DELIVER = 2
    LOAD = 3
    UNLOAD = 4

class Drone:

    id = 0
    state = Status.WAIT

    def __init__(self, id):
        self.id = id

    def goto(self, x, y):
        if (self.state == Status.WAIT):
            print (self.state.value)
            self.calculate(x, y)

    def calculate(self, x, y):
        print (x, y)

drone = Drone(0)
drone.goto(1,1)
