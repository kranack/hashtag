from enum import Enum

class Status(Enum):
    WAIT = 1
    DELIVER = 2
    LOAD = 3
    UNLOAD = 4

class Drone:

    id = 0
    state = Status.WAIT
    position = {}

    def __init__(self, id):
        self.id = id
        self.position = {}

    def goto(self, x, y):
        if (self.state == Status.WAIT):
            print (self.state.value)
            nextCase = self.calculate(x, y)
            self.move(nextCase)

    def move(self, nextCase):
        self.position['x'] = nextCase['x']
        self.position['y'] = nextCase['y']

    def calculate(self, x, y):
        print (x, y)
