import logging
import dramatiq
from apps.core.mail import send_mail
from apps.users.models import User
from .models import Product


logger = logging.getLogger(__name__)


@dramatiq.actor
def email_admin_product_modification(product_id: int, differences: dict):
    logger.error('email_admin_product_modification | product_id: {}'.format(product_id))
    try:
        product_instance = Product.objects.get(id=product_id)
        recipient_list = User.get_admin_emails()
        message = f'Product updated: {product_instance.slug}  |  differences: {differences}'
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
