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

- Python 3.13
- Django 5.2.3

## Setup Instructions

1. **Clone the repository**
```
git clone git@github.com:abdirakhman/remarcable-take-home.git
```

2. **Create a virtual env**
3. **Install dependencies**
```
pip install -r requirements.txt
```
1. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
1. **Create a superuser**
```
python manage.py createsuperuser
```
1. **Load sample data (optional)**
```
python create_sample_data.py
```
1. **Run the development server**
```
python manage.py runserver
```
1. **Access the application**

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

