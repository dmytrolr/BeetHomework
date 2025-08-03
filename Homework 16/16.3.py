class Product:
    def __init__(self, type_: str, name: str, price: float):
        self.type_ = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.total_income = 0.0

    def add_product(self, product, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            price_with_markup = product.price * 1.3
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': price_with_markup,
                'discount': 0
            }

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100.")
        found = False
        for item in self.products.values():
            product = item['product']
            if ((identifier_type == 'name' and product.name == identifier) or
                    (identifier_type == 'type' and product.type_ == identifier)):
                item['discount'] = percent
                found = True
        if not found:
            raise ValueError("Product not found by identifier.")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found.")
        product_data = self.products[product_name]
        if product_data['amount'] < amount:
            raise ValueError("Not enough product in stock.")
        product_data['amount'] -= amount
        discount = product_data.get('discount', 0)
        final_price = product_data['price'] * (1 - discount / 100)
        self.total_income += final_price * amount

    def get_income(self):
        return round(self.total_income, 2)

    def get_all_products(self):
        return [
            {
                'name': name,
                'type': data['product'].type_,
                'price': round(data['price'], 2),
                'amount': data['amount'],
                'discount': data.get('discount', 0)
            }
            for name, data in self.products.items()
        ]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Product not found.")
        return product_name, self.products[product_name]['amount']


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add_product(p, 10)
s.add_product(p2, 300)
s.sell_product('Ramen', 10)

# s.add_product(p, 5)
# assert s.get_product_info('Football T-Shirt') == ('Football T-Shirt', 15)
#
# s.set_discount('Ramen', 25)
# assert any(
#     prod['name'] == 'Ramen' and prod['discount'] == 25
#     for prod in s.get_all_products()
# )
#
# s.set_discount('Sport', 10, identifier_type='type')
# assert any(
#     prod['name'] == 'Football T-Shirt' and prod['discount'] == 10
#     for prod in s.get_all_products()
# )

assert s.get_product_info('Ramen') == ('Ramen', 290)
print("Complete test successful")
