# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160625_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-article_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
