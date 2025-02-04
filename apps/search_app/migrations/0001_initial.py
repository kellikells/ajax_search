# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-10 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('image_path', models.TextField()),
                ('sport', models.IntegerField(choices=[(1, 'Basketball'), (2, 'Volleyball'), (3, 'Baseball'), (4, 'Soccer'), (5, 'Football')], max_length=1)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
