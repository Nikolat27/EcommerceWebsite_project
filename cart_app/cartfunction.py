from django.http import HttpResponse

from product_app.models import Product

CART_SESSION_ID = "cart"


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)

        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Product.objects.get(id=int(item["id"]))
            item['product'] = product
            # price = product.discount_price()
            item['total_price'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id, item['color'])
            yield item

    def unique_id_generator(self, id, color):
        result = f"{id}-{color}"
        return result

    def add(self, product, color, quantity):
        unique = self.unique_id_generator(product.id, color)
        if unique not in self.cart:
            self.cart[unique] = {"quantity": int(quantity), "price": str(product.discount_price()),
                                 "just_discount": str(product.just_discount_price()), "color": str(color),
                                 "id": str(product.id)}
        else:
            self.cart[unique]["quantity"] += int(quantity)

        self.save()

    def update(self, product, color, new_quantity):
        unique = self.unique_id_generator(product.id, color)

        if new_quantity:
            if unique in self.cart:
                self.cart[unique]["quantity"] = int(new_quantity)
            else:
                self.cart[unique] = {"quantity": int(new_quantity), "price": str(product.discount_price()),
                                     "color": str(color),
                                     "id": str(product.id)}
        else:
            print("there is no override quantity")

        self.save()

    def len(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()
        else:
            return HttpResponse("This id is unavailable in cart! cart_function")

    def total(self):
        cart = self.cart.values()
        total = 0
        for item in cart:
            total += int(item['price']) * int(item['quantity'])
        return total

    def total_discount(self):
        cart = self.cart.values()
        total = 0
        for item in cart:
            total += int(item['price']) * int(item['quantity'])
        return total

    def just_discount(self):
        cart = self.cart.values()
        total = 0
        for item in cart:
            total += int(item['just_discount'])
        return total

    def save(self):
        self.session.modified = True

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
