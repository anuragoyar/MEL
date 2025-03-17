from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.crypto import get_random_string

from .models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to handle additional actions when a user is created.
    """
    if created:
        # Generate email verification token
        instance.email_verification_token = get_random_string(64)
        instance.save(update_fields=['email_verification_token'])
        
        # Here you could add code to send a verification email
        # send_verification_email(instance) 