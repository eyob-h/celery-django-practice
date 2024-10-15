from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celery_django_practice import settings
from django.utils import timezone
from datetime import timedelta

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()

    for user in users:
        mail_subject = "Celery Test"
        message = "This test email has been sent from celery!"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"