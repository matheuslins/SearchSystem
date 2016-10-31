# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 21:54
from __future__ import unicode_literals

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
                ('number', models.IntegerField(default=0, verbose_name='Número')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('date_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Box',
                'verbose_name_plural': 'Boxes',
            },
        ),
        migrations.CreateModel(
            name='BoxLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Date and Time of action')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Null'), (1, 'Criado'), (2, 'Atualizado'), (3, 'Deletado')], default=0, verbose_name='Status')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_box', to='core.Box', verbose_name='Box Log')),
            ],
            options={
                'verbose_name': 'Box Log',
                'verbose_name_plural': 'Boxes Logs',
            },
        ),
    ]
