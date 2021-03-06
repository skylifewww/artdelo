# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 08:43
from __future__ import unicode_literals

import article.models
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20160626_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('link', models.CharField(blank=True, default='', max_length=250, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to=article.models.make_upload_path, verbose_name='Изображение')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Короткое описание RU')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Порядок сортировки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
