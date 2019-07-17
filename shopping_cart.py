import purchase

class Cart:

    def __init__(self, total_price, shopping_cart):
        self.shopping_cart = []
        self.total_price = total_price


    # def __str__(self):
    #     return f'''{self.name} {self.base_price}'''

    def add_item_cart(self, new_product):
        self.shopping_cart.append(new_product)
        print(self.shopping_cart)

    def remove_item_cart(self, return_product):
        self.shopping_cart.pop(self.shopping_cart.index(return_product))

    def cost_b4_tax(self):
        for product in self.shopping_cart:
            return self.base_price
    
    def cost_after_tax(self):
        for product in self.shopping_cart:
            return calc_price()
        

# soup = purchase.Purchase('soup', 9, .13)
# print(soup.show_base())


# carted = Cart(soup.calc_price(), [])
# carted.add_item_cart('eggs')
# print(carted.cost_after_tax()) 