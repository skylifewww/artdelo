# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-08 18:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_auto_20160706_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='category_article',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
    ]
