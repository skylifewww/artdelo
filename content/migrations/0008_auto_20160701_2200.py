# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 22:00
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20160701_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Урл')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Короткое описание RU')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Порядок сортировки')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Слайды',
                'verbose_name': 'Слайд',
            },
        ),
        migrations.RenameField(
            model_name='meta',
            old_name='slug',
            new_name='favicon_slug',
        ),
        migrations.RemoveField(
            model_name='meta',
            name='favicon',
        ),
    ]
