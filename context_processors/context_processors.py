from product_app.models import Product, Category, Color
from cart_app.models import Order, OrderItem, Address, Cart


def context_processor(request):
    categories = Category.objects.all()
    colors = Color.objects.all()

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        user_purchase = Order.objects.filter(user=request.user)
        user_purchase_products = OrderItem.objects.filter(order__user=request.user)
        address = Address.objects.filter(user=request.user)
        like = Product.objects.filter(likes__user=request.user)
        return {"cart": cart, "categories": categories, "colors": colors, "user_purchase": user_purchase,
                "user_purchase_products":
                    user_purchase_products, "address_len": len(address), "len_likee": len(like)}
    else:
        return {"categories": categories, "colors": colors}
