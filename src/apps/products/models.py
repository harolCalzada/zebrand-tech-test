from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from apps.core.models import CoreTimeModel


class Brand(CoreTimeModel):
    name = models.CharField(_('name'), max_length=150)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Product(CoreTimeModel):
    slug = models.SlugField(_('slug'), max_length=150, unique=True)
    sku = models.CharField(_('sku'), max_length=12, unique=True)
    name = models.CharField(_('name'), max_length=150)
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=8)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    @property
    def brand_name(self):
        return self.brand.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
