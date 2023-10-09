from product_app.models import Product
from cart_app.cartfunction import Cart


def context_processor(request):
    cart = Cart(request)
    return {"cart": cart}
