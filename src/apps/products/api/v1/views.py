from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from apps.products.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related('brand')
    lookup_field = 'slug'

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
