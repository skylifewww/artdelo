# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='category_article',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='article.Category', verbose_name='Категория'),
        ),
    ]
