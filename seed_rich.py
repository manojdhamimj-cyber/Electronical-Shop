import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Category, Brand, Product, Review

def seed_rich_products():
    print("Expanding all categories with rich products...")

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

    brands_data = ["ApexTech", "Nexus Dynamics", "QuantumSound", "HyperVision", "Vortex Gaming", "FrostTech", "Sony", "Apple", "Samsung", "LG", "Asus ROG", "Bose"]
    brand_map = {}
    for b in brands_data:
        brand, _ = Brand.objects.get_or_create(name=b)
        brand_map[b] = brand

    products = [
        # Mobile Phones
        {
            "name": "Titanium Fold 5 Ultra",
            "slug": "titanium-fold-5-ultra",
            "category": cat_map["mobile-phones"],
            "brand": brand_map["Samsung"],
            "short_description": "7.9-inch 144Hz Dynamic AMOLED, Snapdragon 8 Elite, 1TB Storage.",
            "description": "The ultimate foldable flagship crafted with aerospace-grade titanium framing, 200MP periscope sensor, and all-day silicon-carbon battery.",
            "price": 1899.00,
            "discount_price": 1649.00,
            "image_url": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?auto=format&fit=crop&w=800&q=80",
            "stock": 25,
            "rating": 4.9,
            "review_count": 340,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Display": "7.9 OLED 144Hz", "RAM": "16GB LPDDR5X", "Storage": "1TB NVMe", "Battery": "5400mAh"}
        },
        {
            "name": "AeroPhone Pro Max 5G",
            "slug": "aerophone-pro-max-5g",
            "category": cat_map["mobile-phones"],
            "brand": brand_map["Apple"],
            "short_description": "Super Retina XDR OLED, A18 Pro 3nm Bionic, Action Button, Ceramic Shield.",
            "description": "Precision-milled titanium enclosure with ultra-thin bezels and ProRes 4K 120fps direct log recording capabilities.",
            "price": 1299.00,
            "discount_price": 1199.00,
            "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80",
            "stock": 40,
            "rating": 4.95,
            "review_count": 520,
            "is_featured": True,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Screen": "6.7 XDR OLED", "Camera": "48MP Triple Fusion", "Chipset": "A18 Pro"}
        },
        {
            "name": "Pixel Zenith 9 Ultra",
            "slug": "pixel-zenith-9-ultra",
            "category": cat_map["mobile-phones"],
            "brand": brand_map["ApexTech"],
            "short_description": "Pure AI Computational Photography, 120Hz LTPO, Tensor G4 processor.",
            "description": "Next-generation generative photo magic, uncompressed RAW editing, and 7 years of OS upgrades.",
            "price": 999.00,
            "discount_price": 849.00,
            "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=800&q=80",
            "stock": 18,
            "rating": 4.8,
            "review_count": 195,
            "is_featured": False,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"OS": "Pure Android 15", "Camera": "50MP Dual Tele", "RAM": "12GB"}
        },

        # Laptops
        {
            "name": "CyberBlade 16 Pro Gaming Laptop",
            "slug": "cyberblade-16-pro",
            "category": cat_map["laptops"],
            "brand": brand_map["Asus ROG"],
            "short_description": "Intel Core i9-14900HX, RTX 4090 16GB, 240Hz Mini-LED Display.",
            "description": "Desktop performance packed inside a CNC machined vapor-chamber chassis. Dominate 8K rendering with zero thermal throttling.",
            "price": 3299.00,
            "discount_price": 2799.00,
            "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
            "stock": 12,
            "rating": 4.95,
            "review_count": 210,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"GPU": "RTX 4090 175W", "CPU": "i9-14900HX", "Memory": "64GB DDR5", "Weight": "2.2kg"}
        },
        {
            "name": "StudioBook M3 Max 16",
            "slug": "studiobook-m3-max-16",
            "category": cat_map["laptops"],
            "brand": brand_map["Apple"],
            "short_description": "16-core CPU, 40-core GPU, Liquid Retina XDR 120Hz, 22h battery life.",
            "description": "Built for software architects, 3D animators, and music producers. Extreme power with silent active cooling.",
            "price": 3499.00,
            "discount_price": 3199.00,
            "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80",
            "stock": 15,
            "rating": 4.98,
            "review_count": 480,
            "is_featured": True,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Chip": "M3 Max", "Unified Memory": "48GB", "Display": "16.2 XDR 1600 nits"}
        },

        # Televisions
        {
            "name": "Visionary 77-inch 8K QD-OLED TV",
            "slug": "visionary-77-8k-oled",
            "category": cat_map["televisions"],
            "brand": brand_map["Samsung"],
            "short_description": "True 8K resolution, 144Hz VRR, Dolby Vision IQ, 60W Acoustic Surface.",
            "description": "Experience true black levels with pure quantum dot brightness. Powered by cognitive AI neural processors for cinematic immersion.",
            "price": 4199.00,
            "discount_price": 3499.00,
            "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=800&q=80",
            "stock": 8,
            "rating": 4.85,
            "review_count": 89,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Panel": "77 QD-OLED", "Refresh Rate": "144Hz VRR", "Audio": "Dolby Atmos 4.2.2ch"}
        },
        {
            "name": "Bravia Cinema OLED 65 4K",
            "slug": "bravia-cinema-oled-65-4k",
            "category": cat_map["televisions"],
            "brand": brand_map["Sony"],
            "short_description": "Acoustic Surface Audio+, Perfect for PlayStation 5, Cognitive Processor XR.",
            "description": "Self-illuminating pixels produce billion shades of realistic color with studio mastered presets.",
            "price": 2399.00,
            "discount_price": 1999.00,
            "image_url": "https://images.unsplash.com/photo-1509281373149-e957c6296406?auto=format&fit=crop&w=800&q=80",
            "stock": 14,
            "rating": 4.9,
            "review_count": 160,
            "is_featured": False,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Panel": "4K OLED", "HDMI": "4x HDMI 2.1 (4K 120Hz)", "Audio": "Acoustic Surface"}
        },

        # Headphones
        {
            "name": "AcousticMaster Studio ANC Headphones",
            "slug": "acousticmaster-studio-anc",
            "category": cat_map["headphones"],
            "brand": brand_map["Sony"],
            "short_description": "Lossless Hi-Res LDAC, 60h Battery, Beryllium Drivers, Active Noise Cancelling.",
            "description": "Studio tuning with zero background noise. Handcrafted memory foam lambskin earcups for unmatched acoustic clarity.",
            "price": 449.00,
            "discount_price": 329.00,
            "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
            "stock": 50,
            "rating": 4.9,
            "review_count": 512,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Battery": "60 Hours", "Codec": "LDAC / aptX HD", "Driver": "45mm Beryllium"}
        },
        {
            "name": "QuietComfort Ultra Wireless",
            "slug": "quietcomfort-ultra-wireless",
            "category": cat_map["headphones"],
            "brand": brand_map["Bose"],
            "short_description": "World-class noise cancellation, CustomTune sound calibration, Immersive Spatial Audio.",
            "description": "Legendary comfort for long-haul travel with personalized spatial audio rendering in real time.",
            "price": 429.00,
            "discount_price": 379.00,
            "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&w=800&q=80",
            "stock": 35,
            "rating": 4.8,
            "review_count": 280,
            "is_featured": False,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Noise Cancellation": "Active CustomTune", "Bluetooth": "5.3 Multipoint"}
        },

        # Smartwatches
        {
            "name": "Chronos Titanium Smartwatch Gen 4",
            "slug": "chronos-titanium-smartwatch",
            "category": cat_map["smartwatches"],
            "brand": brand_map["ApexTech"],
            "short_description": "Sapphire Crystal, ECG + Blood Oxygen, 100m Dive Rating, 14-Day Battery.",
            "description": "Sleek biometric endurance watch crafted from solid grade-5 titanium with dual-frequency GPS navigation.",
            "price": 699.00,
            "discount_price": 549.00,
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
            "stock": 30,
            "rating": 4.75,
            "review_count": 140,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Case": "Grade 5 Titanium", "Waterproof": "10 ATM (100m)", "Battery": "14 Days"}
        },
        {
            "name": "Watch Ultra Titanium Ocean Band",
            "slug": "watch-ultra-titanium-ocean",
            "category": cat_map["smartwatches"],
            "brand": brand_map["Apple"],
            "short_description": "3000 nits Always-On display, Dual-frequency GPS, Depth gauge, 72h Low Power mode.",
            "description": "Designed for endurance athletes, outdoor adventurers, and ocean divers with military-grade ruggedness.",
            "price": 799.00,
            "discount_price": None,
            "image_url": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&w=800&q=80",
            "stock": 20,
            "rating": 4.95,
            "review_count": 420,
            "is_featured": False,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Brightness": "3000 nits", "Cellular": "LTE Built-in", "Durability": "MIL-STD 810H"}
        },

        # Gaming
        {
            "name": "Quantum Liquid Rigs RTX 4090",
            "slug": "quantum-liquid-rigs-4090",
            "category": cat_map["gaming"],
            "brand": brand_map["Vortex Gaming"],
            "short_description": "Custom hard-tubing loop, AMD Ryzen 9 7950X3D, 64GB DDR5 6000MHz, 4TB Gen5 SSD.",
            "description": "Engineered for uncompromising 4K 240fps gameplay with handcrafted frosted acrylic distro-plates and silent pump arrays.",
            "price": 4999.00,
            "discount_price": 4499.00,
            "image_url": "https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=800&q=80",
            "stock": 6,
            "rating": 5.0,
            "review_count": 64,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Liquid Loop": "Custom Hardline Dual 360 Rad", "PSU": "1200W Platinum ATX 3.0"}
        },
        {
            "name": "Apex Elite Mechanical Wireless Keyboard",
            "slug": "apex-elite-mechanical-keyboard",
            "category": cat_map["gaming"],
            "brand": brand_map["Vortex Gaming"],
            "short_description": "Hot-swappable Magnetic Hall Effect switches, 8000Hz polling rate, CNC aluminum frame.",
            "description": "Rapid trigger technology with 0.1mm actuation precision and customizable per-key dynamic RGB.",
            "price": 229.00,
            "discount_price": 189.00,
            "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80",
            "stock": 45,
            "rating": 4.85,
            "review_count": 310,
            "is_featured": False,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Switches": "Magnetic Hall Effect", "Polling": "8000Hz Ultra-Low Latency"}
        },

        # Refrigerators
        {
            "name": "FrostMatrix 4-Door Smart French Refrigerator",
            "slug": "frostmatrix-smart-refrigerator",
            "category": cat_map["refrigerators"],
            "brand": brand_map["FrostTech"],
            "short_description": "Dual Inverter Linear Cooling, Internal AI Camera, Multi-Temp Flex Zone.",
            "description": "Keep perishables 3x fresher with independent humidity chambers and smart IoT internal food monitoring.",
            "price": 2799.00,
            "discount_price": 2299.00,
            "image_url": "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
            "stock": 10,
            "rating": 4.85,
            "review_count": 76,
            "is_featured": False,
            "is_flash_sale": True,
            "is_trending": False,
            "specs": {"Capacity": "28 Cu. Ft.", "Finish": "Matte Black Steel", "Cooling": "Dual Inverter"}
        },
        {
            "name": "InstaView Multi-Door Smart Cooling Hub",
            "slug": "instaview-multi-door-smart-hub",
            "category": cat_map["refrigerators"],
            "brand": brand_map["LG"],
            "short_description": "Knock-twice glass panel, Craft Ice maker, UVnano water dispenser, Wi-Fi ThinQ.",
            "description": "See inside without opening the door. Linear cooling keeps temperature fluctuations within ±0.5°C.",
            "price": 3199.00,
            "discount_price": 2799.00,
            "image_url": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=800&q=80",
            "stock": 8,
            "rating": 4.9,
            "review_count": 92,
            "is_featured": True,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Special Feature": "Craft Ball Ice", "Capacity": "30 Cu. Ft.", "Energy": "Energy Star Certified"}
        },

        # Accessories
        {
            "name": "HyperCharge 240W GaN 4-Port Fast Charger",
            "slug": "hypercharge-240w-gan-charger",
            "category": cat_map["accessories"],
            "brand": brand_map["Nexus Dynamics"],
            "short_description": "Power Delivery 3.1, Dual USB-C 140W simultaneous laptop charging, compact GaN tech.",
            "description": "Fast-charge two laptops and two smartphones simultaneously with smart dynamic power distribution.",
            "price": 129.00,
            "discount_price": 99.00,
            "image_url": "https://images.unsplash.com/photo-1622445262464-84b1456045b6?auto=format&fit=crop&w=800&q=80",
            "stock": 70,
            "rating": 4.92,
            "review_count": 450,
            "is_featured": True,
            "is_flash_sale": True,
            "is_trending": True,
            "specs": {"Total Output": "240W Max", "Ports": "3x USB-C + 1x USB-A", "Technology": "GaN V"}
        },
        {
            "name": "Titanium Thunderbolt 4 Pro Dock Station",
            "slug": "titanium-thunderbolt-4-pro-dock",
            "category": cat_map["accessories"],
            "brand": brand_map["Nexus Dynamics"],
            "short_description": "16-in-1 ports, Dual 8K 60Hz display support, 98W host charging, 2.5Gbps Ethernet.",
            "description": "Expand your workstation with full 40Gbps bidirectional transfer speed and anodized aluminum heat dissipation.",
            "price": 349.00,
            "discount_price": 299.00,
            "image_url": "https://images.unsplash.com/photo-1544652478-6653e09f18a2?auto=format&fit=crop&w=800&q=80",
            "stock": 35,
            "rating": 4.88,
            "review_count": 180,
            "is_featured": False,
            "is_flash_sale": False,
            "is_trending": True,
            "specs": {"Transfer Rate": "40Gbps", "Display": "Dual 8K/4K 144Hz", "Ethernet": "2.5G RJ45"}
        }
    ]

    for p_data in products:
        p, created = Product.objects.update_or_create(slug=p_data['slug'], defaults=p_data)
        if created:
            Review.objects.create(
                product=p,
                user_name="Julian Sterling",
                rating=5,
                comment="Unbelievable build quality. Arrived in 24 hours with premium packaging. 10/10!"
            )

    print("All categories populated with rich flagship products!")

if __name__ == '__main__':
    seed_rich_products()
