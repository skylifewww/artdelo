# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 17:30
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20160702_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='work_category',
            field=mptt.fields.TreeForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='works', to='article.Category', verbose_name='Категории'),
        ),
    ]
