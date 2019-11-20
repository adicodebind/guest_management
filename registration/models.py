from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from base.utils import generate_public_id


# Create your models here.
class User(AbstractUser):
    """
    Extended from Abstract User
    List of inherited fields: first_name, last_name, email, username, password
    """
    public_id = models.CharField(max_length=settings.PUBLIC_ID_LENGTH, editable=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.BooleanField(verbose_name="Phone Number", null=True, blank=True)
    email_confirmed = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self, length=settings.PUBLIC_ID_LENGTH)

        if not self.username:
            self.username = self.email

        super().save(*args, **kwargs)


@receiver(signals.post_save, sender=User)
def set_email_confirmed_true_for_superuser(sender, instance, created, **kwargs):
    """
        If user is superuser, then set email confirmed to true
    """

    if created and instance.is_superuser:
        instance.email_confirmed = True
        instance.save()
