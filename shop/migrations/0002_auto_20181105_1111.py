# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodie',
            name='picture',
            field=models.ImageField(blank=True, default=0, null=True, upload_to='static/shop'),
        ),
    ]