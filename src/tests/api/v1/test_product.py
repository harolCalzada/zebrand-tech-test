from http import HTTPStatus
from decimal import Decimal
from django.utils.text import slugify
import pytest


def test_product_list_api(api_client, nightstand_product):
    response = api_client.get('/api/v1/product/')
    total_products = len([nightstand_product])
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['count'] == total_products
    assert response_data['results'][0]['name'] == nightstand_product.name
    assert Decimal(response_data['results'][0]['price']) == nightstand_product.price
    assert response_data['results'][0]['sku'] == nightstand_product.sku
    assert response_data['results'][0]['slug'] == nightstand_product.slug
    assert response_data['results'][0]['brand_name'] == nightstand_product.brand.name


def test_product_detail_api(api_client, nightstand_product):
    response = api_client.get(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['name'] == nightstand_product.name
    assert Decimal(response_data['price']) == nightstand_product.price
    assert response_data['sku'] == nightstand_product.sku
    assert response_data['slug'] == nightstand_product.slug
    assert response_data['brand_name'] == nightstand_product.brand.name


def test_product_view_counter():
    pass


def test_product_create_api(api_client, luuna_brand, admin_user):
    api_client.force_authenticate(user=admin_user)
    name = 'pillow luuna'
    price = 15.20
    sku = 'PILLOW'
    brand = luuna_brand
    data = {
        'name': name,
        'price': price,
        'sku': sku,
        'brand': brand.id
    }
    response = api_client.post('/api/v1/product/', data=data)
    assert response.status_code == HTTPStatus.CREATED
    response_data = response.json()
    assert response_data['name'] == name
    assert Decimal(response_data['price']) == pytest.approx(Decimal(price))
    assert response_data['sku'] == sku
    assert response_data['slug'] == slugify(name)
    assert response_data['brand_name'] == brand.name


def test_product_create_api_unauthorized(api_client):
    response = api_client.post('/api/v1/product/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_product_create_api_forbidden(api_client, common_user):
    api_client.force_authenticate(user=common_user)
    response = api_client.post('/api/v1/product/')
    assert response.status_code == HTTPStatus.FORBIDDEN



def test_create_product_api_notification():
    pass


def test_product_update_api(api_client, admin_user, nooz_brand, nightstand_product):
    api_client.force_authenticate(user=admin_user)
    product = nightstand_product
    new_name = 'nooz nightstand'
    new_price = 20.99
    new_sku = 'NOOZ-NIGHT'
    new_brand = nooz_brand
    data = {
        'name': new_name,
        'price': new_price,
        'sku': new_sku,
        'brand': new_brand.id
    }
    response = api_client.put(f'/api/v1/product/{product.slug}/', data=data, format='json')
    assert response.status_code == HTTPStatus.OK
    response_data = response.json()
    assert response_data['name'] == new_name
    assert Decimal(response_data['price']) == pytest.approx(Decimal(new_price))
    assert response_data['sku'] == new_sku
    assert response_data['brand_name'] == new_brand.name


def test_product_update_api_unauthorized(api_client, nightstand_product):
    response = api_client.put(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_product_update_api_forbidden(api_client, nightstand_product, common_user):
    api_client.force_authenticate(user=common_user)
    response = api_client.put(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_product_update_api_notification():
    pass


def test_product_delete_api(api_client, admin_user, nightstand_product):
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_product_delete_api_unauthorized(api_client, nightstand_product):
    response = api_client.delete(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.UNAUTHORIZED


def test_product_delete_api_forbidden(api_client, nightstand_product, common_user):
    api_client.force_authenticate(user=common_user)
    response = api_client.delete(f'/api/v1/product/{nightstand_product.slug}/')
    assert response.status_code == HTTPStatus.FORBIDDEN


def test_product_delete_api_notification():
    pass