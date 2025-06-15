# Create your views here.
from django.db.models import Count, Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category__id"]  # keep category filter here
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get("category__id")
        tags = self.request.query_params.get(
            "tags__id"
        )  # tags__id can be comma separated

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        if tags:
            tags_list = tags.split(",")
            # filter products with ANY of these tags (OR)
            queryset = queryset.annotate(
                tag_count=Count("tags", filter=Q(tags__id__in=tags_list), distinct=True)
            ).filter(tag_count=len(tags_list))

        return queryset


def product_list_view(request):
    queryset = Product.objects.all()
    category_id = request.GET.get("category__id")
    tags = request.GET.get("tags__id")
    search = request.GET.get("search")

    if category_id:
        queryset = queryset.filter(category__id=category_id)

    if tags:
        tags_list = tags.split(",")
        queryset = queryset.annotate(
            tag_count=Count("tags", filter=Q(tags__id__in=tags_list), distinct=True)
        ).filter(tag_count=len(tags_list))

    if search:
        queryset = queryset.filter(name__icontains=search)

    return render(request, "products/product_list.html", {"products": queryset})
