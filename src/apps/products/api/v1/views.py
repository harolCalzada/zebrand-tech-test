from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from apps.products.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related('brand')
    lookup_field = 'slug'
    public_method_list = ['list', 'retrieve']

    def get_permissions(self):
        if self.action in self.public_method_list:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

