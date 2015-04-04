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
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=100)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, max_length=1000)),
                ('by', models.ForeignKey(related_name='photos_uploaded', to=settings.AUTH_USER_MODEL)),
                ('hash_tags', models.ManyToManyField(to='photos.HashTag')),
                ('likers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='photos_liked')),
                ('user_tags', models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='photos_tagged_in')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='photo',
            field=models.ForeignKey(to='photos.Photo'),
            preserve_default=True,
        ),
    ]
