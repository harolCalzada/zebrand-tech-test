from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from apps.products.models import Product
from apps.products.signals import product_viewed
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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        product_viewed.send(sender='product_viewed', user=request.user, product_slug=instance.slug)
        return super().retrieve(request, *args, **kwargs)
