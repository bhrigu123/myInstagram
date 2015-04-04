# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.ForeignKey(to='location.City', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='dob',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(unique=True, max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
