# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20160626_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_works',
            field=models.ManyToManyField(blank=True, default='', related_name='works', related_query_name='works', to='article.Works', verbose_name='Примеры работ'),
        ),
    ]
