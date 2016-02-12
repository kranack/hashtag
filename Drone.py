from enum import Enum
import math

class Status(Enum):
    WAIT = 1
    DELIVER = 2
    LOAD = 3
    UNLOAD = 4

class Drone:

    id = 0
    state = Status.WAIT
    position = {}
    products = []

    def __init__(self, id, x, y):
        self.id = id
        self.position = {'x': x, 'y': y}

    def goto(self, x, y):
        if (self.state == Status.WAIT):
            print (self.state.value)
            ''' self.calculate(x, y) '''
            self.move({'x': x, 'y': y})

    def fill(self, nbProducts, products):
        self.products.append(products)

    def move(self, nextCase):
        self.position['x'] = nextCase['x']
        self.position['y'] = nextCase['y']

    def calculate(self, x, y):
        return math.ceil(math.sqrt(math.pow((x-self.position['x']), 2) + math.pow((y-self.position['y']), 2)))
