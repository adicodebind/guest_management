from django.db import models


# Create your models here.

class EmailLog(models.Model):
    sender = models.CharField(max_length=100)
    targets = models.TextField()  # comma seperated email IDs
    subject = models.CharField(max_length=200)
    content = models.TextField()
