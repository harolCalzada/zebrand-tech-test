import pytest
from apps.products.models import Product, Brand


def create_brand(name: str) -> Brand:
    return Brand.objects.create(name=name)


@pytest.fixture
def luuna_brand(db) -> Brand:
    return create_brand('Luuna')


@pytest.fixture
def nooz_brand(db) -> Brand:
    return create_brand('Nooz')


def create_product(
    sku,
    name,
    brand: Brand,
    price=10.00,
) -> Product:
    return Product.objects.create(
        sku=sku,
        name=name,
        price=price,
        brand=brand
    )


@pytest.fixture
def nightstand_product(db, luuna_brand) -> Product:
    return create_product(
        sku='NIGHTSTAND',
        name='Nightstand',
        brand=luuna_brand,
        price=100.00
    )
