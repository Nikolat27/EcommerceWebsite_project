from product_app.models import Product
from cart_app.cartfunction import Cart


def context_processor(request):
    cart = Cart(request)      #Never give pass to the context_processor fucntion
    return {"cart": cart}
