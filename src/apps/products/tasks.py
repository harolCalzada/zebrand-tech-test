import logging
import dramatiq
from apps.core.mail import send_mail
from apps.users.models import User
from .models import Product
from .constants import ProductActions


logger = logging.getLogger(__name__)


@dramatiq.actor
def email_admin_product_modification(product_id: int, action: str):
    logger.error('email_admin_product_modification | product_id: {} | action: {}'.format(product_id, action))
    try:
        product_instance = Product.objects.get(id=product_id)
        recipient_list = User.get_admin_emails()
        if action == ProductActions.CREATE:
            message = 'Product created: {}'.format(product_instance.slug)
        elif action == ProductActions.UPDATE:
            message = 'Product updated: {}'.format(product_instance.slug)
        else:
            message = 'Product deleted: {}'.format(product_instance.slug)
    except Product.DoesNotExist:
        logger.error('Product does not exist: {}'.format(product_id))
        return
    try:
        send_mail(
            subject='Product modification',
            message=message,
            recipient_list=recipient_list
        )
    except Exception as e:
        logger.error('Failed to send email: {}'.format(e))

