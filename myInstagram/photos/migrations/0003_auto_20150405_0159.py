# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_auto_20150405_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('photo', models.ForeignKey(to='photos.Photo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comments',
            name='by',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
