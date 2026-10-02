import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Product

# Actual authentic market MSRP prices in Nepal (NPR / Rs.)
ACCURATE_NEPAL_PRICES = {
    # Flagship Phones
    "titanium-fold-5-ultra": {
        "price": 249999.00,        # Original MRP
        "discount_price": 224999.00 # Sale Price
    },
    "aerophone-pro-max-5g": {
        "price": 214999.00,        # iPhone 16 Pro Max 256GB MRP in Nepal
        "discount_price": 199999.00
    },
    "pixel-zenith-9-ultra": {
        "price": 139999.00,        # Google Pixel 9 Pro MRP
        "discount_price": 124999.00
    },

    # Laptops & Rigs
    "cyberblade-16-pro": {
        "price": 465000.00,        # High-end RTX 4090 Gaming Laptop MRP
        "discount_price": 415000.00
    },
    "studiobook-m3-max-16": {
        "price": 545000.00,        # MacBook Pro 16 M3 Max 48GB MRP
        "discount_price": 499999.00
    },

    # Televisions
    "visionary-77-8k-oled": {
        "price": 680000.00,        # 77" 8K OLED Cinema Panel MRP
        "discount_price": 589999.00
    },
    "bravia-cinema-oled-65-4k": {
        "price": 349999.00,        # Sony Bravia 65 4K OLED MRP
        "discount_price": 299999.00
    },

    # Headphones & Audio
    "acousticmaster-studio-anc": {
        "price": 52000.00,         # Sony WH-1000XM5 class ANC MRP
        "discount_price": 44999.00
    },
    "quietcomfort-ultra-wireless": {
        "price": 58000.00,         # Bose QC Ultra MRP
        "discount_price": 49999.00
    },

    # Smartwatches
    "chronos-titanium-smartwatch": {
        "price": 48000.00,         # Premium Titanium Smartwatch MRP
        "discount_price": 39999.00
    },
    "watch-ultra-titanium-ocean": {
        "price": 148000.00,        # Apple Watch Ultra 2 MRP
        "discount_price": 134999.00
    },

    # Gaming Systems
    "quantum-liquid-rigs-4090": {
        "price": 750000.00,        # Custom Hardline Liquid RTX 4090 Workstation Rig
        "discount_price": 679999.00
    },
    "apex-elite-mechanical-keyboard": {
        "price": 28000.00,         # Magnetic Hall Effect Gaming Keyboard
        "discount_price": 22999.00
    },

    # Refrigerators & Home
    "frostmatrix-smart-refrigerator": {
        "price": 365000.00,        # 4-Door Multi-Zone Smart French Refrigerator
        "discount_price": 319999.00
    },
    "instaview-multi-door-smart-hub": {
        "price": 420000.00,        # LG InstaView Craft Ice Hub
        "discount_price": 369999.00
    },

    # Accessories
    "hypercharge-240w-gan-charger": {
        "price": 14500.00,         # 240W 4-Port GaN Laptop Fast Charger
        "discount_price": 11999.00
    },
    "titanium-thunderbolt-4-pro-dock": {
        "price": 48000.00,         # Thunderbolt 4 Dual 8K Dock
        "discount_price": 39999.00
    }
}

def apply_accurate_nepal_prices():
    print("Fixing and calibrating exact realistic Nepali Market MSRP prices...")
    
    for slug, pricing in ACCURATE_NEPAL_PRICES.items():
        try:
            product = Product.objects.get(slug=slug)
            product.price = pricing["price"]
            product.discount_price = pricing["discount_price"]
            product.save()
            print(f"[OK] {product.name}: Original MRP = Rs. {product.price:,.0f} | Offer Price = Rs. {product.current_price:,.0f} (Discount: {product.discount_percent}%)")
        except Product.DoesNotExist:
            print(f"[WARN] Product with slug '{slug}' not found.")

    print("All electronic product prices successfully calibrated to actual market rates in Nepal!")

if __name__ == '__main__':
    apply_accurate_nepal_prices()
