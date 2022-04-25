from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .thread import SendAccountActivationEmail
import random
User = settings.AUTH_USER_MODEL
from .models import Account

SIX_NUMBER = random.randint(100000, 999999)

@receiver(post_save, sender=Account)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            otp = str(SIX_NUMBER)
            instance.otp = otp
            instance.save()
            ''' EXCEUTING THREAD TO SEND EMAIL '''
            SendAccountActivationEmail(instance.email , otp).start()

    except Exception as e:
        print(e)