from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'

    def ready(self) -> None:
        from .receivers import (
            product_update_notification,
            increment_product_view_counter
        )