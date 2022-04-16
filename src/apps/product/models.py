from django.db import models


class Brand(models.Model):
    name = models.CharField('name', max_length=150)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Product(models.Model):
    sku = models.CharField('sku', max_length=30)
    name = models.CharField('name', max_length=150)
    price = models.DecimalField()
    brand = models.ForeignKey(Brand)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
