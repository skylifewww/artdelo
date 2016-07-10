# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-29 12:23
from __future__ import unicode_literals

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20160629_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_back', models.ImageField(blank=True, upload_to=content.models.make_upload_path, verbose_name='Изображение_1200x118')),
                ('text_small', models.CharField(blank=True, max_length=250, verbose_name='Обещание')),
                ('text_big', models.CharField(blank=True, max_length=250, verbose_name='Заявка на победу')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
            ],
            options={
                'verbose_name_plural': 'Шапки',
                'verbose_name': 'Шапка',
            },
        ),
    ]
