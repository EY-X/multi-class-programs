class Purchase:

    def __init__(self, name, base_price, tax_rate):
        self.name = name
        self.base_price = base_price
        self.tax_rate = tax_rate

    def show_base(self):
        return self.base_price


    def calc_price(self):
        calc_price_product = (self.base_price * (self.tax_rate * 0.01)) + self.base_price
        return calc_price_product


        

