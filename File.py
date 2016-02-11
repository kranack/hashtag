class File:

    filename = 0
    nbDrones = 0
    maxTurns = 0
    maxPayload = 0
    nbProducts = 0

    def __init__(self, filename):
        self.filename = filename

    def readFile(self):
        f = open(self.filename,"r")
        limits = f.readline().split()
        lines = int(limits[0])
        col = int(limits[1])
        self.nbDrones = int(limits[2])
        self.maxTurns = int(limits[3])
        self.maxPayload = int(limits[4])
        self.nbProducts = int(f.readline())
        pw = f.readline().split()
        productWeights = [0 for i in range(self.nbProducts)]
        for i in range(self.nbProducts) :
            productWeights[i] = int(pw[i])
        nbWarehouses = int(f.readline())
        # 0 .. self.nbProducts, x-coor, y-coor
        warehouseData = [[0 for i in range(self.nbProducts + 2)] for k in range(nbWarehouses)]
        for k in range(nbWarehouses) :
          wp = f.readline().split()
          warehouseData[k][self.nbProducts] = int(wp[0])
          warehouseData[k][self.nbProducts + 1] = int(wp[1])
          ww = f.readline().split()
          for i in range(self.nbProducts) :
              warehouseData[k][i] = int(ww[i])
        nbOrders = int(f.readline())
        #xcor, ycor, self.nbProducts
        ordersData = [[0,0,0,{}] for i in range(nbOrders)]
        for i in range(nbOrders) :
            cor = f.readline().split()
            ordersData[i][0] = int(cor[0])
            ordersData[i][1] = int(cor[1])
            ordersData[i][2] = int(f.readline()) # c'est le nb des products
            od = f.readline().split()
            for j in range(ordersData[i][2]) :
                q = int(od[j])
                if (q in ordersData[i][3]) :
                    ordersData[i][3][q] += 1
                else :
                    ordersData[i][3][q] = 1
        f.close()
        return ordersData
