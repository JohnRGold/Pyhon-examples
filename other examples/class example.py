class Furniture:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        print("This object's price is USD {:.2f}".format(self.price))

class Table(Furniture):
    def __init__(self, material, legs, surface, shape, price):
        super().__init__(price) # Constructor call to super class
        self.material = material
        self.legs = legs
        self.surface = surface
        self.shape = shape

myTable = Table("wood",4,"1.5m^2","rectangular",60.0)
myTable.get_price()
