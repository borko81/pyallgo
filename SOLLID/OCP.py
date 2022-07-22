class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VipDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2


class SuperVipDiscount(VipDiscount):
    def get_discount(self):
        return super().get_discount() * 2


discounts = {
    'default': lambda x, y: Discount(x, y),
    'vip': lambda x, y: VipDiscount(x, y)
}

internet_user = [
    {'customer': 'Borko', 'price': 100, 'vid': 'default'}
]
name = internet_user[0]['customer']
price = internet_user[0]['price']

u = discounts[internet_user[0]['vid']](name, price)
print(u.get_discount())
