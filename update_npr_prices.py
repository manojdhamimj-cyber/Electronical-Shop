import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Product

def convert_to_nepali_rs():
    print("Updating product prices to realistic Nepali Rupees (NPR / Rs.)...")
    
    # Rate ~135 NPR per USD
    products = Product.objects.all()
    for p in products:
        if p.price < 10000:  # If in original USD scale, multiply by 135
            p.price = round(float(p.price) * 135, -1)
            if p.discount_price:
                p.discount_price = round(float(p.discount_price) * 135, -1)
            p.save()
            print(f"Updated {p.name}: Rs. {p.current_price:,.0f}")

    print("All products successfully converted to Nepali Rupees!")

if __name__ == '__main__':
    convert_to_nepali_rs()
