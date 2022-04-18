import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Product
from .tasks import email_admin_product_modification

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Product)
def product_create_update_notification(sender, **kwargs):
    logger.info('product_create_update_notification: {}'.format(kwargs['instance'].id))
    created = kwargs.get('created', False)
    update_fields = kwargs.get('update_fields', None)
    email_admin_product_modification.send(kwargs['instance'].id, created=created, updated_fields=update_fields)
    # {'signal': <django.db.models.signals.ModelSignal object at 0xffff9f2ae470>, 'instance': <Product: string3>, 'created': True, 'update_fields': None, 'raw': False, 'using': 'default'}


@receiver(post_delete, sender=Product)
def product_delete_notification(sender, **kwargs):
    logger.info('product_delete_notification: {}'.format(kwargs['instance'].id))
    email_admin_product_modification.send(kwargs['instance'].id)
    # kwargs!!! {'signal': <django.db.models.signals.ModelSignal object at 0xffff86ede650>, 'instance': <Product: string3>, 'using': 'default'}