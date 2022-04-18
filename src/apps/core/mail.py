from django.core.mail import send_mail as send_mail_django


def send_mail(subject, message, from_email, recipient_list, fail_silently=False):
    try:
        send_mail_django(
            subject=subject,
            message=message,
            from_email=from_email,   # This will have no effect is you have set DEFAULT_FROM_EMAIL in settings.py
            recipient_list=recipient_list,    # This is a list
            fail_silently=fail_silently     # Set this to False so that you will be noticed in any exception raised
        )
    except Exception as e:
        print(e)
