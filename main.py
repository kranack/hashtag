from __future__ import print_function
import sys
from Drone import Drone
from Warehouse import Warehouse
from File import File

if (len(sys.argv) < 2):
    print('usage: main.py datafile')
else:
    inputFile = File(sys.argv[1])
    datas = inputFile.readFile()
    print(datas)
    drone = Drone(0)
