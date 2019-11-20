# Generated by Django 2.2.7 on 2019-11-20 19:16

import base.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_visitor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[base.validators.phone_number_validator], verbose_name='Phone Number'),
        ),
    ]
