# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 03:41
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name_plural': 'Boxes',
                'verbose_name': 'Box',
            },
        ),
        migrations.CreateModel(
            name='BoxLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time of action')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_box', to='core.Box', verbose_name='Box Log')),
            ],
            options={
                'verbose_name_plural': 'Boxes Logs',
                'verbose_name': 'Box Log',
            },
        ),
    ]