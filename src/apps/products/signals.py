from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Product


@receiver(post_save, sender=Product)
def product_create_update_notification(sender, **kwargs):
    print('kwargs!!!', kwargs)
    # {'signal': <django.db.models.signals.ModelSignal object at 0xffff9f2ae470>, 'instance': <Product: string3>, 'created': True, 'update_fields': None, 'raw': False, 'using': 'default'}


@receiver(post_delete, sender=Product)
def product_delete_notification(sender, **kwargs):
    print('kwargs!!!', kwargs)
    # kwargs!!! {'signal': <django.db.models.signals.ModelSignal object at 0xffff86ede650>, 'instance': <Product: string3>, 'using': 'default'}