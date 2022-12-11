class Product:
    def __init__(self, category, name, price):
        self.category = category
        self.name = name
        self.price = price


class ProductStock:
    def __init__(self, product: Product, amount):
        self.product = product
        self.amount = amount

    def reduce_amount_by(self, number):
        self.amount -= number


class Discount:
    def __init__(self, identifier, percent, identifier_type="name"):
        self.identifier = identifier
        self.percent = percent

        if identifier_type != "name" and identifier_type != "category":
            raise ValueError(
                "identifier_type provided can be either 'name' or 'category' value"
            )

        self.identifier_type = identifier_type

    def discount_for(self, product: Product):
        if getattr(product, self.identifier_type) == self.identifier:
            return self.percent

        return 0


class Order:
    def __init__(self, product: Product, amount, discount):
        self.product = product
        self.amount = amount
        self.discount = discount
        self.total_price = 0.0

    def check_out(self):
        total = self.product.price*1.3 * self.amount
        discount = (self.discount * total) / 100.0
        self.total_price = round(total - discount, 2)

    def get_total_price(self):
        return self.total_price


class ProductStore:
    def __init__(self):
        self.stock = []
        self.orders = []
        self.discount = None

    def add(self, product, amount):
        self.stock.append(ProductStock(product, amount))

    def set_discount(self, identifier, percent, identifier_type):
        self.discount = Discount(identifier, percent, identifier_type)

    def get_product_stock(self, product_name):
        return [stock for stock in self.stock if stock.product.name == product_name][0]

    def get_income(self):
        return sum(map(lambda order: order.get_total_price(), self.orders))

    def get_all_products(self):
        return self.stock

    def get_product_info(self, product_name):
        product_stock = self.get_product_stock(product_name)

        if not product_stock:
            return None

        return (product_stock.product.name, product_stock.amount)

    def sell_product(self, product_name, amount):
        product_stock = self.get_product_stock(product_name)

        if not product_stock:
            raise ValueError("A product with such name does not exist in the store")

        if product_stock.amount < amount:
            raise ValueError("Out of stock")

        product = product_stock.product
        discount_percent = self.discount.discount_for(product) if self.discount else 0
        order = Order(product, amount, discount_percent)

        order.check_out()
        product_stock.reduce_amount_by(amount)
        self.orders.append(order)


p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()

s.set_discount("Football T-Shirt", 20, "name")
s.add(p, 10)
s.add(p2, 300)
s.sell_product("Ramen", 10)
s.sell_product("Football T-Shirt", 5)

assert s.get_product_info("Ramen") == ("Ramen", 290)
assert s.get_income() == 539.5