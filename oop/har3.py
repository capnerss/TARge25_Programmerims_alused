class Computer:

    def __init__(self):
        self.__selling_price = 700

    def sell(self):
        print(f"Selling Price: {self.__selling_price}")

    def set_selling_price(self, price):
        self.__selling_price = price


if __name__ == '__main__':
    c = Computer()
    c.sell()

    # change the price
    c.__selling_price = 1000
    c.sell()

    # setting selling price using setter function
    c.set_selling_price(1000)
    c.sell()