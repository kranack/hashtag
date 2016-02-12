from __future__ import print_function
import sys
from Drone import Drone
from Warehouse import Warehouse
from File import File

def getDrone(x, y):
    return drones[0]

if (len(sys.argv) < 2):
    print('usage: main.py datafile')
else:
    inputFile = File(sys.argv[1])
    datas = inputFile.readFile()
    drones = []
    '''print(datas)'''
    warehouses = datas['warehouses']
    print(warehouses)
    for i in range(datas['drones']):
        drone = Drone(i, warehouses[0][3], warehouses[0][4])
        drones.append(drone)
    for drone in drones:
        distance = 0
        toDeliver = 0
        count = 0
        for order in datas['orders']:
            '''drone = getDrone(order[0], order[1])'''
            newDistance = drone.calculate(order[0], order[1])
            print(newDistance)
            if (count == 0):
                distance = newDistance
                toDeliver = order
            else:
                if (newDistance < distance):
                    distance = newDistance
                    toDeliver = order
            count += 1
        datas['orders'].remove(order)
        drone.fill(toDeliver[2], toDeliver[3])
        drone.goto(toDeliver[0], toDeliver[1])
        toDeliver = 0
        print(drone.products)


    print(drones)
