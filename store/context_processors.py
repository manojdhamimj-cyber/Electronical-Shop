from .models import Category, Product

def cart_and_categories(request):
    categories = Category.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    
    # Calculate cart total
    cart_items = []
    cart_total = 0
    if cart:
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            qty = cart.get(str(product.id), 0)
            item_total = float(product.current_price) * qty
            cart_total += item_total
            cart_items.append({
                'product': product,
                'quantity': qty,
                'total_price': item_total
            })

    wishlist = request.session.get('wishlist', [])

    return {
        'nav_categories': categories,
        'cart_count': cart_count,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'wishlist_count': len(wishlist),
        'wishlist_ids': wishlist,
    }
