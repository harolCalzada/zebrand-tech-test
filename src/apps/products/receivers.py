import logging
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from apps.core.redis import redis_client
from .models import Product
from .tasks import email_admin_product_modification
from .constants import ProductActions
from .signals import product_viewed

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Product)
def product_create_update_notification(sender, **kwargs):
    logger.info('product_create_update_notification: {}'.format(kwargs['instance'].id))
    action = ProductActions.CREATE if kwargs.get('created') else ProductActions.UPDATE
    email_admin_product_modification.send(kwargs['instance'].id, action=action)


@receiver(post_delete, sender=Product)
def product_delete_notification(sender, **kwargs):
    logger.info('product_delete_notification: {}'.format(kwargs['instance'].id))
    action = ProductActions.DELETE
    email_admin_product_modification.send(kwargs['instance'].id, action=action)


@receiver(product_viewed)
def increment_product_view_counter(sender, user, product_slug: str, **kwargs):
    if user.is_anonymous:
        logger.info('increment_product_view_counter')
        client = redis_client()
        if client.exists(product_slug):
            client.incr(product_slug)
        else:
            client.set(product_slug, 1)
        logger.info('product: {} counter: {}'.format(product_slug, client.get(product_slug)))
