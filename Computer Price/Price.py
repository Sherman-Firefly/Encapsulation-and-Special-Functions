class computer:
    def __init__(self):
        self.__maxprice=1000

    def sell(self):
        print("Selling price: ", self.__maxprice)
    def mxprice(self, price):
        self.__maxprice=price

c=computer()
c.sell()

c.__maxprice=1200
c.sell()

c.mxprice(4000)
c.sell()