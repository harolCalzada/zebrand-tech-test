from django.core.mail import send_mail as send_mail_django
from django.conf import settings


def send_mail(subject, message, recipient_list, fail_silently=False):
    try:
        send_mail_django(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=fail_silently
        )
    except Exception as e:
        print(e)
