from django.db import models
from registration.models import Visitor
from django.conf import settings
from base.utils import generate_public_id, generate_random_string
from django.utils import timezone


# Create your models here.
def get_visitor_token():
    return generate_random_string(5, num_only=True)


class VisitorLog(models.Model):
    visitor_user = models.ForeignKey(to=Visitor, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=settings.PUBLIC_ID_LENGTH, editable=False, unique=True)
    address = models.TextField()
    checkin_time = models.DateTimeField(default=timezone.now)
    checkout_time = models.DateTimeField(null=True)
    unique_token = models.CharField(max_length=4, default=get_visitor_token)

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = generate_public_id(self, length=settings.PUBLIC_ID_LENGTH)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['checkin_time']
