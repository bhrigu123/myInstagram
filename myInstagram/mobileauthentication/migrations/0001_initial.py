# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('token', models.CharField(unique=True, max_length=100)),
                ('status', models.CharField(choices=[('E', 'Expired'), ('V', 'Valid')], default='V', max_length=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('expires_on', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
