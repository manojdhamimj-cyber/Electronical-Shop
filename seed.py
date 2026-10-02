import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Brand, Product, Review

def seed_database():
    print("Seeding initial enterprise electronics data...")
    
    # Create superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@electronical.shop', 'admin123')
        print("Superuser created: username='admin', password='admin123'")

    # Categories
    categories_data = [
        {"name": "Mobile Phones", "slug": "mobile-phones", "icon_svg": "📱", "description": "Flagship 5G smartphones & foldable displays"},
        {"name": "Laptops", "slug": "laptops", "icon_svg": "💻", "description": "High-performance creator workstations and ultrabooks"},
        {"name": "Televisions", "slug": "televisions", "icon_svg": "📺", "description": "4K & 8K QD-OLED cinema displays with high refresh rates"},
        {"name": "Headphones", "slug": "headphones", "icon_svg": "🎧", "description": "Audiophile grade ANC wireless audio and studio monitors"},
        {"name": "Smartwatches", "slug": "smartwatches", "icon_svg": "⌚", "description": "Titanium sapphire biometric smartwatches"},
        {"name": "Gaming", "slug": "gaming", "icon_svg": "🎮", "description": "Custom liquid cooled desktop rigs, consoles and peripherals"},
        {"name": "Refrigerators", "slug": "refrigerators", "icon_svg": "🧊", "description": "Smart IoT multi-zone cooling systems"},
        {"name": "Accessories", "slug": "accessories", "icon_svg": "⚡", "description": "GaN chargers, thunderbolt docks and cables"},
    ]

    cat_map = {}
    for c in categories_data:
        cat, _ = Category.objects.get_or_create(slug=c['slug'], defaults=c)
        cat_map[c['slug']] = cat

    # Brands
    brands_data = ["ApexTech", "Nexus Dynamics", "QuantumSound", "HyperVision", "Vortex Gaming", "FrostTech"]
    brand_map = {}
    for b in brands_data:
        brand, _ = Brand.objects.get_or_create(name=b)
        brand_map[b] = brand

    # Products
    products_data = [
        {
            "name": "Titanium Fold 5 Ultra",
            "slug": "titanium-fold-5-ultra",
            "category": cat_map["mobile-phones"],
            "brand": brand_map["ApexTech"],
            "short_description": "7.9-inch 144Hz Dynamic AMOLED, Snapdragon 8 Elite, 1TB Storage.",
            "description": "The ultimate foldable flagship crafted with aerospace-grade titanium framing, 200MP periscope sensor, and all-day silicon-carbon battery.",
            "price": 1899.00,
            "discount_price": 1699.00,
            "image_url": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?auto=format&fit=crop&w=800&q=80",
            "stock": 15,
            "rating": 4.9,
            "review_count": 340,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Display": "7.9 OLED 144Hz", "RAM": "16GB LPDDR5X", "Storage": "1TB NVMe", "Battery": "5400mAh"}
        },
        {
            "name": "CyberBlade 16 Pro Gaming Laptop",
            "slug": "cyberblade-16-pro",
            "category": cat_map["laptops"],
            "brand": brand_map["Vortex Gaming"],
            "short_description": "Intel Core i9-14900HX, RTX 4090 16GB, 240Hz Mini-LED Display.",
            "description": "Desktop performance packed inside a CNC machined vapor-chamber cooled chassis. Dominate AAA gaming and 8K rendering with zero thermal throttling.",
            "price": 3299.00,
            "discount_price": 2899.00,
            "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
            "stock": 8,
            "rating": 4.95,
            "review_count": 210,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"GPU": "RTX 4090 175W", "CPU": "i9-14900HX", "Memory": "64GB DDR5", "Weight": "2.2kg"}
        },
        {
            "name": "Visionary 77-inch 8K QD-OLED TV",
            "slug": "visionary-77-8k-oled",
            "category": cat_map["televisions"],
            "brand": brand_map["HyperVision"],
            "short_description": "True 8K resolution, 144Hz VRR, Dolby Vision IQ, 60W Acoustic Surface.",
            "description": "Experience true black levels with pure quantum dot brightness. Powered by cognitive AI neural processors for unrivaled cinematic home theater immersion.",
            "price": 4199.00,
            "discount_price": 3599.00,
            "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=800&q=80",
            "stock": 5,
            "rating": 4.8,
            "review_count": 89,
            "is_featured": True,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Panel": "77 QD-OLED", "Refresh Rate": "144Hz VRR", "Audio": "Dolby Atmos 4.2.2ch"}
        },
        {
            "name": "AcousticMaster Studio ANC Headphones",
            "slug": "acousticmaster-studio-anc",
            "category": cat_map["headphones"],
            "brand": brand_map["QuantumSound"],
            "short_description": "Lossless Hi-Res LDAC, 60h Battery, Beryllium Drivers, Active Noise Cancelling.",
            "description": "Studio tuning with zero background noise. Handcrafted memory foam lambskin earcups for unmatched acoustic clarity.",
            "price": 449.00,
            "discount_price": 349.00,
            "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
            "stock": 42,
            "rating": 4.9,
            "review_count": 512,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Battery": "60 Hours", "Codec": "LDAC / aptX HD", "Driver": "45mm Beryllium"}
        },
        {
            "name": "Chronos Titanium Smartwatch Gen 4",
            "slug": "chronos-titanium-smartwatch",
            "category": cat_map["smartwatches"],
            "brand": brand_map["ApexTech"],
            "short_description": "Sapphire Crystal, ECG + Blood Oxygen, 100m Dive Rating, 14-Day Battery.",
            "description": "Sleek biometric endurance watch crafted from solid grade-5 titanium with dual-frequency GPS navigation.",
            "price": 699.00,
            "discount_price": None,
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
            "stock": 25,
            "rating": 4.7,
            "review_count": 140,
            "is_featured": True,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Case": "Grade 5 Titanium", "Waterproof": "10 ATM (100m)", "Battery": "14 Days"}
        },
        {
            "name": "FrostMatrix 4-Door Smart French Refrigerator",
            "slug": "frostmatrix-smart-refrigerator",
            "category": cat_map["refrigerators"],
            "brand": brand_map["FrostTech"],
            "short_description": "Dual Inverter Linear Cooling, Internal AI Camera, Multi-Temp Flex Zone.",
            "description": "Keep perishables 3x fresher with independent humidity chambers and smart IoT internal food monitoring.",
            "price": 2799.00,
            "discount_price": 2399.00,
            "image_url": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
            "stock": 10,
            "rating": 4.85,
            "review_count": 76,
            "is_featured": False,
            "is_flash_sale": True,
            "is_trending": False,
            "specs": {"Capacity": "28 Cu. Ft.", "Finish": "Matte Black Steel", "Cooling": "Dual Inverter"}
        },
    ]

    for p_data in products_data:
        p, created = Product.objects.get_or_create(slug=p_data['slug'], defaults=p_data)
        
        # Add sample reviews
        if created:
            Review.objects.create(
                product=p,
                user_name="Marcus Vance",
                rating=5,
                comment="Absolutely world-class hardware quality. Fast shipping and the performance exceeds expectations!"
            )
            Review.objects.create(
                product=p,
                user_name="Elena Rostova",
                rating=5,
                comment="The design and attention to detail feels like pure luxury. Best tech purchase of the year."
            )

    print("Successfully seeded catalog with flagship categories, brands, products, and reviews!")

if __name__ == '__main__':
    seed_database()
