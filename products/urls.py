# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, product_list_view

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("api/", include(router.urls)),
    path("products/html/", product_list_view, name="product_list_html"),
]
