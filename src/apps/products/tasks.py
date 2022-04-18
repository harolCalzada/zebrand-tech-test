import dramatiq

from .models import Product


@dramatiq.actor
def email_admin_product_modification(product_id: int, created: bool = False, updated_fields: dict = {}):
    product = Product.objects.get(id=product_id)
