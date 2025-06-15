# Django Product Catalog

A Django application for managing and filtering products with categories and tags.

## Features

- Product management with categories and tags
- Search functionality by product name and description
- Filter by category
- Filter by multiple tags
- Django admin interface for data management
- Responsive product grid display

## Requirements

- Python 3.8+
- Django 4.2.7

## Setup Instructions

1. **Clone the repository**
2. **Create a virtual env**
3. **Install dependencies**
4. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
5. **Create a superuser**
```
python manage.py createsuperuser
```
6. **Load sample data (optional)**
```
python create_sample_data.py
```
7. **Run the development server**
```
python manage.py runserver
```
8. **Access the application**

Main application: http://localhost:8000/
Admin interface: http://localhost:8000/admin/

9. **Access GET products REST API**
http://localhost:8000/api/products/

10. **Access html template**
http://localhost:8000/products/html/

11. **Testing**
```
python manage.py test
```

