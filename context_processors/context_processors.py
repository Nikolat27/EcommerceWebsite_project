from product_app.models import Product, Category, Color
from cart_app.cartfunction import Cart
from cart_app.models import Order, OrderItem


def context_processor(request):
    cart = Cart(request)  # Never give pass to the context_processor fucntion
    categories = Category.objects.all()
    colors = Color.objects.all()
    if request.user.is_authenticated:
        user_purchase = Order.objects.filter(user=request.user)
        user_purchase_products = OrderItem.objects.filter(order__user=request.user)
        return {"cart": cart, "categories": categories, "colors": colors, "user_purchase": user_purchase,
                "user_purchase_products":
                    user_purchase_products}
    else:
        return {"cart": cart, "categories": categories, "colors": colors, "categories1": categories1}
