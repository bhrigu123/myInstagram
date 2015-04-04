# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150404_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(null=True, max_length=128, unique=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='street_address',
            field=models.CharField(null=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
