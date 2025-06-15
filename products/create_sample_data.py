import os
import random
from decimal import Decimal

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from products.models import Category, Product, Tag  # noqa: E402 because of Django setup

# Clear existing data
Product.objects.all().delete()
Category.objects.all().delete()
Tag.objects.all().delete()

# Create Categories
categories = [
    "Electronics",
    "Books",
    "Clothing",
    "Home & Garden",
    "Sports & Outdoors",
]

category_objects = []
for name in categories:
    category = Category.objects.create(name=name)
    category_objects.append(category)
    print(f"Created category: {name}")

# Create Tags
tag_names = [
    "New Arrival",
    "Best Seller",
    "On Sale",
    "Premium",
    "Eco-Friendly",
    "Limited Edition",
    "Trending",
    "Budget-Friendly",
    "Professional",
    "Beginner-Friendly",
]

tag_objects = []
for tag_name in tag_names:
    tag = Tag.objects.create(name=tag_name)
    tag_objects.append(tag)
    print(f"Created tag: {tag_name}")

# Create Products
products_data = [
    # Electronics
    (
        "Smartphone X Pro",
        "Latest flagship smartphone with advanced camera system and 5G connectivity",
        899,
        0,
    ),
    (
        "Wireless Earbuds Pro",
        "Premium noise-cancelling wireless earbuds with 30-hour battery life",
        249,
        0,
    ),
    (
        '4K Smart TV 55"',
        "Ultra HD smart television with HDR support and built-in streaming apps",
        699,
        0,
    ),
    (
        "Gaming Laptop",
        "High-performance laptop with RTX graphics for gaming and content creation",
        1499,
        0,
    ),
    # Books
    (
        "Python Programming Guide",
        "Comprehensive guide to Python programming for beginners and experts",
        49,
        1,
    ),
    (
        "The Art of Coding",
        "Best practices and design patterns for clean, maintainable code",
        39,
        1,
    ),
    (
        "Web Development Mastery",
        "Full-stack web development with modern frameworks and tools",
        59,
        1,
    ),
    (
        "Data Science Handbook",
        "Complete reference for data analysis and machine learning",
        69,
        1,
    ),
    # Clothing
    (
        "Premium Cotton T-Shirt",
        "Comfortable 100% organic cotton t-shirt in various colors",
        29,
        2,
    ),
    (
        "Denim Jeans Classic",
        "Classic fit denim jeans with stretch comfort technology",
        79,
        2,
    ),
    (
        "Running Shoes Pro",
        "Professional running shoes with advanced cushioning system",
        129,
        2,
    ),
    (
        "Winter Jacket Extreme",
        "Waterproof insulated jacket for extreme weather conditions",
        199,
        2,
    ),
    # Home & Garden
    (
        "Smart Home Hub",
        "Central control system for all your smart home devices",
        149,
        3,
    ),
    (
        "Garden Tool Set",
        "Complete 15-piece stainless steel garden tool collection",
        89,
        3,
    ),
    (
        "LED Desk Lamp",
        "Adjustable LED lamp with touch controls and USB charging",
        49,
        3,
    ),
    (
        "Air Purifier Pro",
        "HEPA air purifier for large rooms with smart sensors",
        299,
        3,
    ),
    # Sports & Outdoors
    (
        "Yoga Mat Premium",
        "Extra thick non-slip yoga mat with alignment guides",
        39,
        4,
    ),
    (
        "Camping Tent 4-Person",
        "Waterproof family tent with easy setup and ventilation",
        179,
        4,
    ),
    (
        "Fitness Tracker Advanced",
        "Water-resistant fitness tracker with heart rate monitoring",
        99,
        4,
    ),
    (
        "Mountain Bike Pro",
        "Professional mountain bike with 21-speed gear system",
        799,
        4,
    ),
]

for name, description, price, category_index in products_data:
    product = Product.objects.create(
        name=name,
        description=description,
        price=Decimal(str(price)),
        category=category_objects[category_index],
    )

    # Add random tags (1-3 tags per product)
    num_tags = random.randint(1, 3)
    random_tags = random.sample(tag_objects, num_tags)
    product.tags.add(*random_tags)

    print(f"Created product: {name}")

print("\nSample data created successfully!")
print(f"Total categories: {Category.objects.count()}")
print(f"Total tags: {Tag.objects.count()}")
print(f"Total products: {Product.objects.count()}")
