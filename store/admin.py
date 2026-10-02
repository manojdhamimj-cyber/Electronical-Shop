from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Category, Brand, Product, Review, Order, OrderItem

def dashboard_callback(request, context):
    context.update({
        "total_products": Product.objects.count(),
        "total_orders": Order.objects.count(),
        "recent_orders": Order.objects.order_by('-created_at')[:5],
    })
    return context

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ['name', 'website']
    search_fields = ['name']

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'discount_price', 'stock', 'rating', 'is_flash_sale', 'is_trending']
    list_filter = ['category', 'brand', 'is_flash_sale', 'is_trending', 'is_featured']
    search_fields = ['name', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ReviewInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'phone', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'phone']
    inlines = [OrderItemInline]

@admin.register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = ['product', 'user_name', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
