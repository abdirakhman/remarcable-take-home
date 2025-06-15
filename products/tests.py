from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from .models import Category, Product, Tag
from .views import ProductViewSet


class ProductViewTests(TestCase):
    def setUp(self):
        # Create categories
        self.cat1 = Category.objects.create(name="Cat1")
        self.cat2 = Category.objects.create(name="Cat2")

        # Create tags
        self.tag1 = Tag.objects.create(name="Tag1")
        self.tag2 = Tag.objects.create(name="Tag2")
        self.tag3 = Tag.objects.create(name="Tag3")

        # Create products
        self.prod1 = Product.objects.create(
            name="Product One", price=2000, category=self.cat1
        )
        self.prod1.tags.add(self.tag1, self.tag2)

        self.prod2 = Product.objects.create(
            name="Product Two", price=10000, category=self.cat1
        )
        self.prod2.tags.add(self.tag2)

        self.prod3 = Product.objects.create(
            name="Another Product", price=5000, category=self.cat2
        )
        self.prod3.tags.add(self.tag3)

        self.prod4 = Product.objects.create(
            name="Fourth Product", price=9999, category=self.cat2
        )
        # No tags for prod4

        self.factory = APIRequestFactory()

    def test_viewset_filter_by_category(self):
        request = self.factory.get("/products/?category__id=%d" % self.cat1.id)
        view = ProductViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # All products in cat1
        product_ids = [p["id"] for p in response.data]
        self.assertIn(self.prod1.id, product_ids)
        self.assertIn(self.prod2.id, product_ids)
        self.assertNotIn(self.prod3.id, product_ids)
        self.assertNotIn(self.prod4.id, product_ids)

    def test_viewset_filter_by_single_tag(self):
        request = self.factory.get(f"/products/?tags__id={self.tag1.id}")
        view = ProductViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_ids = [p["id"] for p in response.data]
        # Only prod1 has tag1
        self.assertIn(self.prod1.id, product_ids)
        self.assertNotIn(self.prod2.id, product_ids)
        self.assertNotIn(self.prod3.id, product_ids)

    def test_viewset_filter_by_multiple_tags(self):
        # prod1 has tag1 and tag2, prod2 only tag2
        tags_param = f"{self.tag1.id},{self.tag2.id}"
        request = self.factory.get(f"/products/?tags__id={tags_param}")
        view = ProductViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_ids = [p["id"] for p in response.data]
        # Only prod1 has BOTH tags
        self.assertIn(self.prod1.id, product_ids)
        self.assertNotIn(self.prod2.id, product_ids)
