import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.contrib import messages
from .models import Category, Product, Brand, Order, OrderItem, Review

def home_view(request):
    featured_products = Product.objects.filter(is_featured=True)[:8]
    flash_sale_products = Product.objects.filter(is_flash_sale=True)[:6]
    trending_products = Product.objects.filter(is_trending=True)[:8]
    categories = Category.objects.all()
    brands = Brand.objects.all()
    recent_reviews = Review.objects.select_related('product').order_by('-created_at')[:6]

    context = {
        'featured_products': featured_products,
        'flash_sale_products': flash_sale_products,
        'trending_products': trending_products,
        'categories': categories,
        'brands': brands,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'store/index.html', context)

def product_list_view(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    brand_id = request.GET.get('brand', '')
    sort_by = request.GET.get('sort', 'newest')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(brand__name__icontains=query)
        )

    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    if brand_id:
        products = products.filter(brand_id=brand_id)

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'rating':
        products = products.order_by('-rating')
    else:
        products = products.order_by('-created_at')

    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'brands': brands,
        'current_category': current_category,
        'query': query,
        'sort_by': sort_by,
        'selected_brand': brand_id,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'store/product_list.html', context)

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    reviews = product.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        rating = int(request.POST.get('rating', 5))
        comment = request.POST.get('comment')
        if user_name and comment:
            Review.objects.create(
                product=product,
                user_name=user_name,
                rating=rating,
                comment=comment
            )
            return redirect('store:product_detail', slug=product.slug)

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
    }
    return render(request, 'store/product_detail.html', context)

def cart_view(request):
    return render(request, 'store/cart.html')

def add_to_cart_view(request, product_id):
    cart = request.session.get('cart', {})
    str_id = str(product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart[str_id] = cart.get(str_id, 0) + quantity
    request.session['cart'] = cart
    request.session.modified = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        total_count = sum(cart.values())
        return JsonResponse({'status': 'success', 'cart_count': total_count})

    return redirect(request.META.get('HTTP_REFERER', 'store:cart'))

def update_cart_view(request, product_id):
    cart = request.session.get('cart', {})
    str_id = str(product_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        cart[str_id] = quantity
    else:
        cart.pop(str_id, None)

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('store:cart')

def remove_from_cart_view(request, product_id):
    cart = request.session.get('cart', {})
    str_id = str(product_id)
    cart.pop(str_id, None)
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('store:cart')

def toggle_wishlist_view(request, product_id):
    wishlist = request.session.get('wishlist', [])
    if product_id in wishlist:
        wishlist.remove(product_id)
        added = False
    else:
        wishlist.append(product_id)
        added = True
    
    request.session['wishlist'] = wishlist
    request.session.modified = True

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success', 'added': added, 'wishlist_count': len(wishlist)})
    return redirect(request.META.get('HTTP_REFERER', 'store:home'))

def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('store:product_list')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        payment_method = request.POST.get('payment_method', 'Card')

        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total_amount = sum(float(p.current_price) * cart[str(p.id)] for p in products)

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            postal_code=postal_code,
            payment_method=payment_method,
            total_amount=total_amount,
            status='Processing'
        )

        for product in products:
            qty = cart[str(product.id)]
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.current_price,
                quantity=qty
            )
            if product.stock >= qty:
                product.stock -= qty
                product.save()

        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'store/order_success.html', {'order': order})

    return render(request, 'store/checkout.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        messages.success(request, f"Thank you {name}! Your message has been received.")
        return render(request, 'store/contact.html', {'success': True})
    return render(request, 'store/contact.html')

def terms_view(request):
    return render(request, 'store/terms.html')

def pwa_manifest_view(request):
    manifest = {
        "name": "Electronical Enterprise Shop",
        "short_name": "Electronical",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#0F172A",
        "theme_color": "#2563EB",
        "icons": [
            {
                "src": "/static/images/icon-192.png",
                "sizes": "192x192",
                "type": "image/png"
            },
            {
                "src": "/static/images/icon-512.png",
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }
    return HttpResponse(json.dumps(manifest), content_type="application/json")
