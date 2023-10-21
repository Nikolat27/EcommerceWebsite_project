from product_app.models import Product, Category, Color
from cart_app.cartfunction import Cart


def context_processor(request):
    cart = Cart(request)      #Never give pass to the context_processor fucntion
    categories = Category.objects.filter(parent=None)
    colors = Color.objects.all()
    return {"cart": cart, "categories": categories, "colors": colors}
