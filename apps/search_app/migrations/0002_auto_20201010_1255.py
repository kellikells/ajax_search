# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-10-10 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sport',
            field=models.IntegerField(choices=[(1, 'Basketball'), (2, 'Volleyball'), (3, 'Baseball'), (4, 'Soccer'), (5, 'Football')]),
        ),
    ]
