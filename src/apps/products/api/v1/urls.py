from django.urls import path
from .views import ProductListAPIView, ProductRetrieveAPIView


urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name='product_list'),
    path("product/<slug:slug>/", ProductRetrieveAPIView.as_view(), name="product_detail"),
]
