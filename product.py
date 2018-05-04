class product(object):
    def __init__(self, price, item_name, wieght, brand, reason):
        self.price = price
        self.item_name = item_name
        self.wieght = wieght
        self.brand = brand
        self.reason = reason
        self.status = "for sale"

        def sell(self):
            if self.status == "for sale":
                self.status = "sold"

        def add_tax(self):
            self.tax = 0.4
            total = self.price * self.Tax
            return total

        def get_back(self):
            if self.reason == "defective":
                self.status = "defective"
                self.price = 0
            elif self.reason == "new":
                self.status = "for sale"
            else:
                self.status = "used"
                self.price = self.price * 0.2

        def displayInfo(self):
            print "Product info:" + self.price + str(self.item_name)
            print "continued.."  + self.wieght + str(self.brand) + self.status

item1 = product(3, "buzz lightyear", 0.5, "pixar", "new")
item1.get_back()
