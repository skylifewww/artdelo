# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20160701_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='published',
            field=models.BooleanField(default=0, verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='meta',
            name='favicon_slug',
            field=models.CharField(blank=True, max_length=250, verbose_name='Урл favicon'),
        ),
    ]
