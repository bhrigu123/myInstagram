# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='hash_tags',
            field=models.ManyToManyField(to='photos.HashTag', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='likers',
            field=models.ManyToManyField(related_name='photos_liked', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='user_tags',
            field=models.ManyToManyField(related_name='photos_tagged_in', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
