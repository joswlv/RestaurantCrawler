# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlist',
            name='mangoRatingValue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantlist',
            name='restaurantAddress',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
