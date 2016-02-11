class Warehouse:

    id = 0
    products = {}

    def __init__(self, id):
        self.id = id
        self.products = {}

    def addProduct(self, product):
        if (product['type'] in self.products.keys()):
            self.products[product['type']] += product['nb']
        else:
            self.products[product['type']] = product['nb']

    def removeProduct(self, product):
        ''' TODO: Vérifier que le nombre de products n'est pas inférieur à 0 '''
        if (product['type'] in self.products.keys()):
            self.products[product['type']] -= product['nb']
