from django.db import models
from django.utils.translation import gettext as _
from apps.core.models import CoreTimeModel


class Brand(CoreTimeModel):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Product(CoreTimeModel):
    sku = models.CharField(_('sku'), max_length=30)
    name = models.CharField(_('name'), max_length=150)
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=8)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
