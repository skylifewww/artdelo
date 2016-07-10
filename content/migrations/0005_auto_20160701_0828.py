# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 08:28
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_top_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='top',
            name='meta_author',
            field=models.CharField(blank=True, max_length=250, verbose_name='Автор сайта'),
        ),
        migrations.AddField(
            model_name='top',
            name='meta_description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Мета описание'),
        ),
        migrations.AddField(
            model_name='top',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=250, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='top',
            name='meta_title',
            field=models.CharField(blank=True, max_length=250, verbose_name='Заголовок в браузере'),
        ),
    ]
