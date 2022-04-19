import logging
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Product
from .tasks import email_admin_product_modification
from .signals import product_viewed
from .services import increment_product_view_counter as increment_product_view_counter_service
from .utils import get_differences_between_product_instances

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=Product)
def product_update_notification(sender, **kwargs):
    if not kwargs.get('created', False):
        new_instance = kwargs['instance']
        logger.info('product_create_update_notification: {}'.format(new_instance.id))
        previous = Product.objects.get(id=new_instance.id)
        differences = get_differences_between_product_instances(previous, new_instance)
        email_admin_product_modification.send(kwargs['instance'].id, differences)


@receiver(product_viewed)
def increment_product_view_counter(sender, user, product_slug: str, **kwargs):
    if user.is_anonymous:
        logger.info('increment_product_view_counter')
        view_count = increment_product_view_counter_service(product_slug)
        logger.info('product: {} counter: {}'.format(product_slug, view_count))
